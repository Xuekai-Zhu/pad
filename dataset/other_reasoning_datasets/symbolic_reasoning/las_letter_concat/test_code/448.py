def solution():
    s = "Stevie Julie Leonard Karina"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())