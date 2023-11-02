def solution():
    s = "Elise Lupe Renee Noemi"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())