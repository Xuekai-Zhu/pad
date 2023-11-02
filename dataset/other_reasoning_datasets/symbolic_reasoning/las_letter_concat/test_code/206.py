def solution():
    s = "Nico Lorenzo Johanna Teresita"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())