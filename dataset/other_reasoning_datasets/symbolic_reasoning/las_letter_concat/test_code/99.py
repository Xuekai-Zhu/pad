def solution():
    s = "Desmond Camille Joana Garcia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())