def solution():
    s = "Morgan Perla Joao Marta"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())