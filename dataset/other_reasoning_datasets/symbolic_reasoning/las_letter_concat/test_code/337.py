def solution():
    s = "Chance Valentin Micah Clara"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())