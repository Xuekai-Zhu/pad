def solution():
    s = "Adrian Marlon Karla Florence"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())