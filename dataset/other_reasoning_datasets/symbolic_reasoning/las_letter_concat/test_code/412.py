def solution():
    s = "Kathy Elsa Alba Ivette"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())