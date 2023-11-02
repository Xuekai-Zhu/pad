def solution():
    s = "Sterling Jenifer Patsy Denise"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())