from pymsgprompt.prompt import log


def perror(message, file=None):
    log(message, logtype='error', timestamp=True, file=file, reset=True)


def pwarn(message, file=None):
    log(message, logtype='warn', timestamp=True, file=file, reset=True)


def pinfo(message, file=None):
    log(message, logtype='info', timestamp=True, file=file, reset=True)



