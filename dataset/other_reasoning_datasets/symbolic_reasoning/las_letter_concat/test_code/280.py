def solution():
    s = "Leanne Lulu Lopez Jp"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())