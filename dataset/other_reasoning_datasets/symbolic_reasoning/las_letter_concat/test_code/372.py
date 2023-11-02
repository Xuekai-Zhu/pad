def solution():
    s = "Tori Mariam Gaby Brayan"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())