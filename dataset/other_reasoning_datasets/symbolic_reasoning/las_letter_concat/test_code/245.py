def solution():
    s = "Belkis Wendell Lissette Patricia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())