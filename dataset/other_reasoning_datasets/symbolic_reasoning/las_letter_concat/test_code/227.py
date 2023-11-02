def solution():
    s = "Héctor Daniela Rossy Jose Manuel"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())