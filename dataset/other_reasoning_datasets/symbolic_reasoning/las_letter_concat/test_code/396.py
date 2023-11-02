def solution():
    s = "Niki Graham Vernon Beau"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())