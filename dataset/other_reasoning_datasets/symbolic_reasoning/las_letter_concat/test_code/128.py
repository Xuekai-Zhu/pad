def solution():
    s = "Timmy Katherine Gabriel Nate"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())