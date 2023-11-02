def solution():
    s = "Candy Megan Ed Nathan"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())