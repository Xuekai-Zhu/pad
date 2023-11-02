def solution():
    s = "Noelle Byron Jane Darin"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())