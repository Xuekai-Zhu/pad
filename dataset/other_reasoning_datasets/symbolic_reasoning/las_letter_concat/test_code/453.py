def solution():
    s = "Eugenia Kellie Quentin Mike"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())