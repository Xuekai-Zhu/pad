def solution():
    s = "Tim Candace Cecil Misael"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())