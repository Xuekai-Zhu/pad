def solution():
    s = "Garrett Eva Joaquin Monique"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())