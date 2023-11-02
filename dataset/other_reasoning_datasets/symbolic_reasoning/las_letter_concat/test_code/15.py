def solution():
    s = "Annie Toño Sharon Delores"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())