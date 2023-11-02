def solution():
    s = "Zach Trenton Cary Beth"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())