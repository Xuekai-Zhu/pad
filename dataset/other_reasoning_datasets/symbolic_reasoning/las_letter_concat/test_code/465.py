def solution():
    s = "Cassie Clifton Erik Everardo"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())