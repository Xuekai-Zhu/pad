def solution():
    s = "Carolyn Sasha Mercy Keri"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())