def solution():
    s = "Chloe Flaco Theodore Nathalie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())