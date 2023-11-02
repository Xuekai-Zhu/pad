def solution():
    s = "Tere Niko Keith Conner"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())