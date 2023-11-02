def solution():
    s = "Dan Ruth Xavier Isidro"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())