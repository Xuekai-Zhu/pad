def solution():
    s = "Emanuel Cheyenne Perez Yvette"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())