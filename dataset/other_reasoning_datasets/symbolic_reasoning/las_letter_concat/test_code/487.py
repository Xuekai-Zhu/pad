def solution():
    s = "Andre Oralia Carrie Bruno"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())