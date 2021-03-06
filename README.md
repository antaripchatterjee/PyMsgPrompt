# PyMsgPrompt

PyMsgPrompt is a python module to embed prompt functionality in your code.

## Version

The current version of this module is `1.3.0` and this is the third BETA release after first BETA version `1.2.2`, however, you can run the below command to check the version of the module.

```bash
python -m pymsgprompt.version
```

## Platform Supports

This is a cross platform module and supported both in python 2 and 3.

## Installation

To install this module you can use clone with git or just simply run pip install command.

### Using git

```bash
git clone https://github.com/antaripchatterjee/PyMsgPrompt.git
cd PyMsgPrompt
python setup.py install
```

### Using pip

```bash
pip install pymsgprompt
```

## Uninstallation

Uninstallation can be done by running pip uninstall command.

```bash
pip uninstall pymsgpropmt
```

## Usage

To test this module, you can run the below simple code.

```python
from pymsgprompt.prompt import ask, log
from pymsgprompt.logger import perror, pinfo, pwarn
import time
if __name__ == '__main__':
    answer = ask('Do you want to close?', choices=['yes', 'no', 'not sure'], default='yes', timestamp=True, regexp=True, ignore_case=False)
    # with open('test.txt', 'w') as test:
    #     print (log('Answer is %s'%answer, logtype='error', timestamp=True, file=test))
    if answer.startswith('n'):
        log('Answer is %s'%answer, logtype='error', timestamp=False, reset=True)
    else:
        log('Answer is %s'%answer, logtype='info', timestamp=False, reset=True)
    for i in range(1000, 0, -1):
        log('The message is %d'%i, timestamp=True, end=None if i > 1 else '\n', reset=i==1)
        time.sleep(0.01)
    
    pinfo('I am a Python Developer')
    pwarn('Some kind of warning message')
    perror('Some kind of error message')
```

Below is the output,

```output
[QUES] 2021-Apr-01 22:27:50: Do you want to close? (yes/ no/ not sure)[yes]not
not sure
Answer is not sure
[INFO] 2021-Apr-01 22:28:11: The message is 1   
[INFO] 2021-Apr-01 22:28:11: I am a Python Developer
[WARN] 2021-Apr-01 22:28:11: Some kind of warning message
[ERROR] 2021-Apr-01 22:28:11: Some kind of error message
```

## API Reference

`pymsgprompt.prompt.ask` function takes two positional arguments `on_success` and `on_error`, and they expect two callback functions, which will be called after validating the answer. The default value of them are `pymsgprompt.handler.default_on_success` and `pymsgprompt.handler.default_on_error` respectively.

The callback function for `on_success` takes three arguments, which are `question`, `actual_answer` and `original_answer`. The `ask` function returns the same value, actually returned by the callback function. The default function returns the `original_answer`.

The callback function for `on_error` takes four arguments, which are `question`, `choices`, `default`, and `error`. This value must return either `True`, means the question should be reasked, or `False`, means no need to ask the question again. The default function returns the `False`.

A good documentation, specially for the developers, will be provided later.

## License

This module is licensed under [MIT License](https://github.com/antaripchatterjee/PyMsgPrompt/blob/master/LICENSE).

## Contribution

Pull requests are always awesome, but please make sure of raising request, before making any changes.