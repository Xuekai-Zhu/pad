def solution():
    s = "Jaime Brad Levi Emmanuel"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())