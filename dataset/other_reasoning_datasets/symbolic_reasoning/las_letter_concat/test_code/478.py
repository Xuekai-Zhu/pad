def solution():
    s = "Noelia Cassidy Ashok Francisco"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())