def swap_case(s):
    result=[]
    for char in s:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
