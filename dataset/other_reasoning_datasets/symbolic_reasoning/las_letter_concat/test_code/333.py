def solution():
    s = "Ace Rosy Kimberly Jean"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())