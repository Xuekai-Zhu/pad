def solution():
    s = "Kristen Herbert Benny El"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())