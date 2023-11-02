def solution():
    s = "Gerson Roxanne Deborah Nathaniel"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())