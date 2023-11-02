def solution():
    s = "Oswaldo José Luis Sheldon Tara"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())