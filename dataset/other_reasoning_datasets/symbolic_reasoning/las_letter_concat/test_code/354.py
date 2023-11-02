def solution():
    s = "Philip Antony Iris Alicia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())