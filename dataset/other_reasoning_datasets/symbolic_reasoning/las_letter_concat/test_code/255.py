def solution():
    s = "Shawn Tracie Lynne Leila"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())