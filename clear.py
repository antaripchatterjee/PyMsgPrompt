import shutil
from os import path, sys, remove
from glob import glob

if __name__ == '__main__':
    self_dir = path.dirname(__file__)
    for dir in ['build', 'dist', 'PyMsgPrompt.egg-info']:
        shutil.rmtree(
            path.abspath(
                path.join(
                    self_dir,
                    dir
                )
            ),
            ignore_errors=True,
            onerror= lambda func, _path, exception : sys.stdout.write('{0} could not be deleted : {1}\n'.format(_path, exception))
        )
    shutil.rmtree(
        path.abspath(
            path.join(
                self_dir,
                'pymsgprompt',
                '__pycache__'
            )
        ),
        ignore_errors=True,
        onerror= lambda func, _path, exception : sys.stdout.write('{0} could not be deleted : {1}\n'.format(_path, exception))
    )
    for f in glob(path.abspath(path.join(self_dir, 'pymsgprompt', '*.pyc'))):
        remove(f)