def solution():
    s = "Mel Josh Alejandra Harley"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())