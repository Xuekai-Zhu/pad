def solution():
    s = "Deandre Moe Jack Vanessa"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())