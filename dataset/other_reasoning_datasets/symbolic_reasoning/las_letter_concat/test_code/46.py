def solution():
    s = "Cheri Rico Teo Jesus"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())