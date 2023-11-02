def solution():
    s = "Estrella Madison Paco Rj"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())