def solution():
    s = "Craig Dillon Troy Griselda"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())