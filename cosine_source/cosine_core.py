""" This file defines all the core functionality in cosine algorithm for text matching """
import re
import math
from collections import Counter
import cosine_source.cosine_logging as cl
WORD = re.compile(r'\w+')
LOG = cl.get_logger()


def get_cosine(vec1, vec2):
    """ Function used for getting the cosine value
    vec1, vec2: Input vector from the texts to be compared """
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        cosine_value = 0.0
    else:
        cosine_value = float(numerator / denominator)
    LOG.info("get_cosine() value:%f", cosine_value)
    return cosine_value


def text_to_vector(text):
    """ Function used for converting the text to vector
    text: Input text """
    words = WORD.findall(text)
    return Counter(words)


def check_tolerance(actual_val, exp_val):
    """ Function used for checking the tolerance value (defaulted to 100)
    actual_val: what is the actual value after processing the cosine
    exp_val: what is the expected value for the cosine """
    if actual_val >= exp_val:
        tolerance_value = abs(actual_val - exp_val) <= 1
    else:
        tolerance_value = 0
    LOG.info("check_tolerance() value:%d", tolerance_value)
    return tolerance_value
