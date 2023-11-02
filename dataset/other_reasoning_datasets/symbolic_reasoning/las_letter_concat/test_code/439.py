def solution():
    s = "Antonio Ronald Ken Rachael"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())