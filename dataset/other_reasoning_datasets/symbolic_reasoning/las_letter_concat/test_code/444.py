def solution():
    s = "Georgina Joshua Lindsey César"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())