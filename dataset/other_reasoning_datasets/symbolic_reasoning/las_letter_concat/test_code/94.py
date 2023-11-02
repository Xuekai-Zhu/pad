def solution():
    s = "Salma Pj Gladis Monica"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())