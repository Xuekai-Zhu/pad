def solution():
    s = "Virginia Juanita Zak Wayne"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())