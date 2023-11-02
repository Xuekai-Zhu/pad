def solution():
    s = "Itzel Anderson Kenia Edy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())