def solution():
    s = "Lazaro Ana Charlotte Precious"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())