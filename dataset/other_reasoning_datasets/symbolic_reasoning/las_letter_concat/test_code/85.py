def solution():
    s = "Chantal Ines Valeria Francesca"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())