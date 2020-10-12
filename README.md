# PyMsgPrompt

PyMsgPrompt is a python module to embed prompt functionality in you your code.

## Version

The current version is `0.0.3` and this is the first Alpha release.

## Platform Supports

This is a cross platform module and also supports python 2 and 3.

## Installation

To install this module you can use clone with git or just simply run pip install command.

### Using git

```bash
git clone https://github.com/antaripchatterjee/PyMsgPrompt.git
cd PyMsgPrompt
python setup.py install
```

## Uninstallation

Uninstallation can be done by running pip uninstall command.

```bash
pip uninstall pymsgpropmt
```

## Usage

To test this module, you can run the below simple code.

```python
from pymsgprompt.prompt import ask

if __name__ == '__main__':
    answer = ask('Do you want to close?', choices=['yes', 'no', 'yesss'], default='no', logtype=False, regexp=True, ignore_case=False)
    print(answer)
```

## API Reference

A good documentation, specially for the developers, will be provided later.

## Development Areas

I am already working on some other functionality, which will be provided in the future releases.

## License

This module is licensed under MIT license.

## Contribution

Pull requests are always awesome, but please make sure of raising request, before making any changes.