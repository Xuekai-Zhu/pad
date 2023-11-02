def solution():
    s = "Marcus Ramirez Junior Arely"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())