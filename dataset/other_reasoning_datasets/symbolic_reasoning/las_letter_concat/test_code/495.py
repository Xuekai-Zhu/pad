def solution():
    s = "Marlen Sonja Anita Dale"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())