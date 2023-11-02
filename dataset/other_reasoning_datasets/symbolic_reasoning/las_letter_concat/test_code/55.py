def solution():
    s = "Julieta Zachary Jared Tyson"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())