def solution():
    s = "Kelly Cheryl Nancy Jojo"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())