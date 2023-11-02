def solution():
    s = "Alina Alessandra Amina Bianca"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())