def solution():
    s = "Antoine Javier Brett Stewart"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())