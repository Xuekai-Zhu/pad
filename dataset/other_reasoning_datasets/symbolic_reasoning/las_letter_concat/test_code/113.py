def solution():
    s = "Anastasia Thelma Sheri Rosita"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())