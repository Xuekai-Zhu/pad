def solution():
    s = "Noah Aubrey Cesar Eliana"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())