def solution():
    s = "Salvador Sol Tyler Kareem"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())