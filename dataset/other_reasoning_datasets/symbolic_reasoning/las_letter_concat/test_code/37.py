def solution():
    s = "Billy Kassandra Joy Abe"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())