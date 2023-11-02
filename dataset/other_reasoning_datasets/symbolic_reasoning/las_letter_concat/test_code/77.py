def solution():
    s = "Amparo Gianna Dion Tessa"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())