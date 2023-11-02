def solution():
    s = "Ron Carl Joann Young"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())