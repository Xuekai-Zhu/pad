def solution():
    s = "Star Jude Rosemarie Raquel"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())