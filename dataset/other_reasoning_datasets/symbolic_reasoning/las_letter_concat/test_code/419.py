def solution():
    s = "Andres Mary Ann Sydney Dina"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())