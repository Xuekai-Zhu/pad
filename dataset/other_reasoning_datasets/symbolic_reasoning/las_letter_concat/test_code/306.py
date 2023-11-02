def solution():
    s = "Rosa Lana Curtis Rae"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())