def solution():
    s = "Buddy Violet Johana Tina"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())