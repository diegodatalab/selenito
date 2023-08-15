import logging


def log_details():
    logging.basicConfig(
        filename="demo.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
    )
    return logging.getLogger()


logger = log_details()
logger.info("Program execution started")

a = 4
b = 3

if a > b:
    print('Diego')
    logger.info('a is greater than b, hence Diego got printed in output')

logger.info("Program execution ended")