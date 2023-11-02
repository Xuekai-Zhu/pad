def solution():
    s = "Lizzy Juany Aisha Brenda"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())