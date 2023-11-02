def solution():
    s = "Glen Ariana Reggie Polo"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())