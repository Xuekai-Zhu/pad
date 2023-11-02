def solution():
    s = "June Robin Josie Bo"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())