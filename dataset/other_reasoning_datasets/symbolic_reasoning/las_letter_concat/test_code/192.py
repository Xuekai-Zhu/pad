def solution():
    s = "Martin Sage Tanisha Rick"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())