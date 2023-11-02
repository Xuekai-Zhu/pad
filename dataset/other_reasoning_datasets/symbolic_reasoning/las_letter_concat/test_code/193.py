def solution():
    s = "Suzanne Julissa Chino America"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())