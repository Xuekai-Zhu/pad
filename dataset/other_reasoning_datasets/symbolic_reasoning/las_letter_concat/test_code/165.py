def solution():
    s = "Fernanda Magda Elmer Alvaro"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())