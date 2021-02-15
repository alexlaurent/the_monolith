def try_me():
    print('Do you wish to know your future?')
    ans = input()
    if ans == 'yes' or ans == 'y':
        return "\n Don't be a fool, your future is yours to build"
    else:
        return "\n Good,go build it"
if __name__ == "__main__":
    print(try_me())