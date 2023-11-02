def solution():
    s = "Breanna Trey Omar Patrice"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())