def solution():
    s = "Rogelio Freddy Ivan Madeleine"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())