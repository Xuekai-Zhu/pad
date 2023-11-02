def solution():
    s = "Sabrina Pete Mary La"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())