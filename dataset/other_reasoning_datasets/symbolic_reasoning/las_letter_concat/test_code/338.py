def solution():
    s = "Dusty Yanet Hortencia Lili"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())