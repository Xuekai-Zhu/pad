def solution():
    s = "Debora Jayson Donna Sai"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())