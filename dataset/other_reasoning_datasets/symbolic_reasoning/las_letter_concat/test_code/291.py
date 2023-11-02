def solution():
    s = "Miranda Jacques Clarence Chandra"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())