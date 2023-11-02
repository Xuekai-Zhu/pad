def solution():
    s = "Laila Audrey Glenn Rhonda"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())