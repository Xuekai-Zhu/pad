def solution():
    s = "Lilian Ian Bryce Aracely"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())