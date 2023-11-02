def solution():
    s = "Conrad Marcella Annette Esteban"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())