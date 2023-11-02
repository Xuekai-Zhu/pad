def solution():
    s = "Ivy Romeo Jana Ej"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())