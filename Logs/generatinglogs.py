import logging

logging.basicConfig(filename="/Volumes/Macintosh HD/For Mac/python project/pythongrid/Logs/logfile.log",format='%(asctime)s: %(levelname)s: %(message)s',
                    filemode='w',level=logging.INFO)
log = logging.getLogger()

log.info("this is our first log")