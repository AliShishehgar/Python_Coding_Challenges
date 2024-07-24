def split_and_join(s):
    result=s.split()
    return "-".join(result)

if __name__ == '__main__':
    s = input()
    result = split_and_join(s)
    print(result)
