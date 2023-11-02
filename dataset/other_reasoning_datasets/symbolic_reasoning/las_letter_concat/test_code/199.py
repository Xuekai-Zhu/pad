def solution():
    s = "Dana German Alvin Braden"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())