def solution():
    s = "Nick Ada Stephany Suzie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())