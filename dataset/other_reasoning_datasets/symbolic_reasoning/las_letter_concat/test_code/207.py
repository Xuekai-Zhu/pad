def solution():
    s = "Paulo Tatyana Bernice Raúl"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())