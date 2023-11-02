def solution():
    s = "Leticia Jacinto Natasha Raphael"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())