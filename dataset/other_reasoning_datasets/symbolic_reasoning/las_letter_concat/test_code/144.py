def solution():
    s = "Arthur Shan Norman Manny"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())