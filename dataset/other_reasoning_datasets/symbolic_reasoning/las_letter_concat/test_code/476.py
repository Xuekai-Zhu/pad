def solution():
    s = "Agnes Adrienne Haley Riley"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())