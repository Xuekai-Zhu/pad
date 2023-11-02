def solution():
    s = "Ángel Carlton Sameer Martinez"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())