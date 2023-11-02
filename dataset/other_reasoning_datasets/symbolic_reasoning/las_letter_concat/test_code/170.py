def solution():
    s = "Tucker Daniel Hernandez Alison"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())