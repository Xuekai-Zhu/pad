def solution():
    s = "Boris Sabina Kaitlyn Cameron"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())