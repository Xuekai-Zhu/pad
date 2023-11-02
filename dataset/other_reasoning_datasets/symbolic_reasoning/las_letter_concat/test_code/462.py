def solution():
    s = "Geovanny Tom Katelyn Jennifer"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())