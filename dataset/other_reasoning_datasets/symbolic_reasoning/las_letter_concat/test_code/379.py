def solution():
    s = "Violeta Clay Janelle Mac"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())