def solution():
    s = "Gee Joseluis Cory Stefanie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())