def solution():
    s = "Leon Payton Stefan Javi"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())