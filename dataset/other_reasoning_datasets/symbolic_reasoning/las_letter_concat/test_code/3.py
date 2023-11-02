def solution():
    s = "Angelina Layla Jenny Zane"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())