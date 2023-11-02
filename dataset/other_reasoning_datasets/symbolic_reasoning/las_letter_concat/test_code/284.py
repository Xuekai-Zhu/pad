def solution():
    s = "Missy Erin Lorna Lenny"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())