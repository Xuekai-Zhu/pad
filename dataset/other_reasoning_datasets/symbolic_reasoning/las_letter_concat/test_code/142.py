def solution():
    s = "Emilia Jonas Christi Sophia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())