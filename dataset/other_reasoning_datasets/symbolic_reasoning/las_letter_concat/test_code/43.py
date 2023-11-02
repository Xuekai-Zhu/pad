def solution():
    s = "Isela Leslie Stacy Ingrid"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())