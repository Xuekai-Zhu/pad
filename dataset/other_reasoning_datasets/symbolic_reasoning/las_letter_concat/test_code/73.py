def solution():
    s = "Janet Ant Vickie Elias"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())