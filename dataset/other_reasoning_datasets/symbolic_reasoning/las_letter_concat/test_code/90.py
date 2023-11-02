def solution():
    s = "Victoria Aurora Amalia Princess"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())