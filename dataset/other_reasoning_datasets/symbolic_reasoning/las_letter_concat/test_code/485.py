def solution():
    s = "Jason Betty Elisa Jay"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())