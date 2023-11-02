def solution():
    s = "Juan Manuel Benjamin Rory Rafael"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())