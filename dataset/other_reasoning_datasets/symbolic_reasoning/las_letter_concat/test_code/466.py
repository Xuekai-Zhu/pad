def solution():
    s = "Pauline Kerry Jeannette Hope"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())