def solution():
    s = "Bj Rigo Nigel Christian"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())