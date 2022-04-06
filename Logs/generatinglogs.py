import logging
## Generating logs
# logging.basicConfig(filename="/Volumes/Macintosh HD/For Mac/python project/pythongrid/Logs/logfile.log",format='%(asctime)s: %(levelname)s: %(message)s',
#                     filemode='w',level=logging.INFO)
# log = logging.getLogger()
#
# log.info("this is our first log")


def log():
    logging.basicConfig(filename="/Volumes/Macintosh HD/For Mac/python project/pythongrid/Logs/logfile.log",
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        filemode='w', level=logging.INFO)


    log = logging.getLogger()
    return log


logging =  log()
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')