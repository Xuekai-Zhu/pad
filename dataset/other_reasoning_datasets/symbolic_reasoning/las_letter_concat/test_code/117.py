def solution():
    s = "Carla Dolores Cooper Damion"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())