def solution():
    s = "Celso Tracy Winston Anton"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())