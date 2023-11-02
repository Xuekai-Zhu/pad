def solution():
    s = "Latoya Eliseo Trina Melisa"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())