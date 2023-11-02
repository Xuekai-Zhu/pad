def solution():
    s = "Gayle Doreen Chelsey Helena"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())