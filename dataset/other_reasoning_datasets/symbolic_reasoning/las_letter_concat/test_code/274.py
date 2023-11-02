def solution():
    s = "Damian Crystal Nisha Hernan"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())