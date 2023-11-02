def solution():
    s = "Yvonne Rafaela Jb Salomon"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())