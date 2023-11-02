def solution():
    s = "Salvatore Gustavo Jill Celeste"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())