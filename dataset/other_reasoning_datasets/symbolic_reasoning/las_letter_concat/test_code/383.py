def solution():
    s = "Emely Chelsea Vladimir Tyrone"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())