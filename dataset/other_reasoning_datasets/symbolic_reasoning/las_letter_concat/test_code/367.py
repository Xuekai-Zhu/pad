def solution():
    s = "Mabel Estela Irene May"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())