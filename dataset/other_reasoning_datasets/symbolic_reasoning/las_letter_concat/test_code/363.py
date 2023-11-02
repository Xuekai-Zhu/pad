def solution():
    s = "Mercedes Adela Susana Rose"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())