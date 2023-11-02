def solution():
    s = "Jermaine Pat Tammie Olivia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())