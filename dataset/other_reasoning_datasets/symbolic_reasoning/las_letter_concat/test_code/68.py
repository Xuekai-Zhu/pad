def solution():
    s = "Chava Rosalia Kurt Linda"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())