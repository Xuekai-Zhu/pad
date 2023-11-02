def solution():
    s = "Frank Trevor Al Gabriella"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())