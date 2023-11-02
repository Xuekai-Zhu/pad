def solution():
    s = "Kyra Luciano Ciara Bryan"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())