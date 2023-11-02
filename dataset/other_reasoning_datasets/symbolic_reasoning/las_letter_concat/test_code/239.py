def solution():
    s = "Mari Ximena Leo Antonia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())