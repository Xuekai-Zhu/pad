def solution():
    s = "Mya Fernando Bubba Tommy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())