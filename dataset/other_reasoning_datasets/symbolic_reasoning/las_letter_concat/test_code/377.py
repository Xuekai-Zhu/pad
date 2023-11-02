def solution():
    s = "Thomas Cara Nita Frances"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())