from pymsgprompt.prompt import ask

if __name__ == '__main__':
    answer = ask('Do you want to close?', choices=['yes', 'no', 'yesss'], default='no', logtype=False, regexp=True, ignore_case=False)
    print(answer)