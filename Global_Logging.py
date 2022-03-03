import logging,os

from datetime import datetime

def get_curr_date():
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y")
    return dt_string

def log(message,type='I'):
    if type == 'D':
        logging.debug(message)
    elif type == 'I':
        logging.info(message)
    elif type == 'E':
        logging.error(message)
    elif type == 'W':
        logging.warning(message)
    elif type == 'E1':
        logging.error("Exception ",exc_info=1)
    print(message)

def set_logger(FileName):
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    handler = logging.FileHandler(FileName, 'w', 'utf-8')
    formatter = logging.Formatter('%(name)s %(message)s') # or whatever
    handler.setFormatter(formatter) # Pass handler as a parameter, not assign
    root_logger.addHandler(handler)
    root_logger.disabled = False


def enable_logger(p_value):
    logger = logging.getLogger()
    if p_value == 'E':
        logger.disabled = True
    else:
        logger.disabled = False

def init_logs(dirname):
    Logdirname = os.path.join(dirname,'outdir')
    if not os.path.exists(Logdirname):
        os.mkdir(Logdirname)
    LogFile = os.path.join(Logdirname,f'Logfile_{get_curr_date()}.log') 
    set_logger(LogFile)
    return LogFile