def solution():
    s = "Paula Irina Laurel Maribel"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())