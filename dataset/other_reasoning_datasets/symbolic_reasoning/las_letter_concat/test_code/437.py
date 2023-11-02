def solution():
    s = "Drew Jhon Jayden Cliff"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())