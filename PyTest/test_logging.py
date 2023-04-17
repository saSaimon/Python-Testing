import logging

def test_logging():

        logger = logging.getLogger(__name__)



        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object into it

        logger.setLevel(logging.CRITICAL)
        logger.debug("A debug statement is executed.")
        logger.info("Information statement.")
        logger.warning("Something is in warning mode.")
        logger.error("A major error has happened.")
        logger.critical("Critical issue.")