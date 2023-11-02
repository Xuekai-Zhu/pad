def solution():
    s = "Adalberto Jamal Carter Robyn"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())