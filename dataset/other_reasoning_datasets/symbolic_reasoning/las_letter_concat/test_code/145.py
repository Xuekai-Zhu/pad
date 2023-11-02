def solution():
    s = "Abdi Clyde Ana Maria Pepe"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())