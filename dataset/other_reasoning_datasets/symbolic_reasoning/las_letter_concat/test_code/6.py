def solution():
    s = "Jesse Roderick Travis Rita"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())