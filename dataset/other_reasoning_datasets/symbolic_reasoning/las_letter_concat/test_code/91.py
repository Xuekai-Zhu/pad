def solution():
    s = "Alec Arianna Corina Juancarlos"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())