def reverseString(string):
    if len(string) == 1:
        return string
    return string[-1] + reverseString(string[:-1])

print(reverseString("yoyo mastery"))

