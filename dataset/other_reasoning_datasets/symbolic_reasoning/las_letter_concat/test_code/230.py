def solution():
    s = "Tiara Araceli Michaela Genaro"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())