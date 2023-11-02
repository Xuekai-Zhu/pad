def solution():
    s = "Leandro Maricela Genevieve Lesly"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())