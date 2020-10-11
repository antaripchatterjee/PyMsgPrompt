from pyask.ask import ask

if __name__ == '__main__':
    answer = ask('Do you want to close', choices=['yes', 'no'], default='no', logtype=True, regexp=True)
    print(answer)