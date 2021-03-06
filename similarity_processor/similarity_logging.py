"""importing module"""
import os
import logging


def get_logger():
    """Create and configure logger"""

    logging.basicConfig(filename=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,
                                                              "similarity_processor",
                                                              "text_similarity.log")),
                        format='%(asctime)s %(message)s', filemode='a')
    # Creating log Object
    __logger = logging.getLogger()
    # Setting the threshold of logger to DEBUG
    __logger.setLevel(logging.DEBUG)
    return __logger
