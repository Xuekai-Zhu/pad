def solution():
    s = "Carole William Tiffany Hilary"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())