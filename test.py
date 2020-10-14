from pymsgprompt.prompt import ask, log
from pymsgprompt.logger import perror, pinfo, pwarn
import time
if __name__ == '__main__':
    answer = ask('Do you want to close?', choices=['yes', 'no', 'yesss'], default='no', timestamp=True, regexp=True, ignore_case=False)
    # with open('test.txt', 'w') as test:
    #     print (log('Answer is %s'%answer, logtype='error', timestamp=True, file=test))
    if answer.startswith('n'):
        log('Answer is %s'%answer, logtype='error', timestamp=False, reset=True)
    else:
        log('Answer is %s'%answer, logtype='info', timestamp=False, reset=True)
    for i in range(1000, 0, -1):
        log('The message is %d'%i, timestamp=True, end=None)
        time.sleep(0.01)
    
    pinfo('I am a Python Developer')
    pwarn('Some kind of warning message')
    perror('Some kind of error message')