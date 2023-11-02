def solution():
    s = "Brandon Ivonne Jefferson Isabella"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())