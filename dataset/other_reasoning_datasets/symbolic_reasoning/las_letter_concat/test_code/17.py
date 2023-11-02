def solution():
    s = "Jorge Natalia Bryant Kiran"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())