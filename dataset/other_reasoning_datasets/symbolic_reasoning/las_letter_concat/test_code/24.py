def solution():
    s = "Billie Paloma Tanner Raul"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())