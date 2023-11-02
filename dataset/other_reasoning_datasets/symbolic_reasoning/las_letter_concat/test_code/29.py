def solution():
    s = "Jacky Socorro Mark Wanda"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())