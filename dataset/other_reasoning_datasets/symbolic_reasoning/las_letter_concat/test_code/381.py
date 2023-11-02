def solution():
    s = "Jenni Leonel Micheal Kat"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())