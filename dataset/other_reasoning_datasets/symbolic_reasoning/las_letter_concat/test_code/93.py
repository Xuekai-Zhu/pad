def solution():
    s = "Selena Keisha Gladys Cedric"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())