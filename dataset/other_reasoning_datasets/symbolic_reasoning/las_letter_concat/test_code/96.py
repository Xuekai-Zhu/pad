def solution():
    s = "Letty Aimee Elvia Ted"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())