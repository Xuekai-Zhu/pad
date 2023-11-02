def solution():
    s = "Abel Mallory Theresa Quinn"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())