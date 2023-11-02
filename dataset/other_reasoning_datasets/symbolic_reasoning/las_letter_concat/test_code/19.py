def solution():
    s = "Melody Ramiro Humberto Jacob"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())