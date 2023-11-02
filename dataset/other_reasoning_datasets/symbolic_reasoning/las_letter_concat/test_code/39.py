def solution():
    s = "Ale Gaspar Sonny Simon"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())