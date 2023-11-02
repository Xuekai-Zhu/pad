def solution():
    s = "Kelvin Brennan Carina Paty"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())