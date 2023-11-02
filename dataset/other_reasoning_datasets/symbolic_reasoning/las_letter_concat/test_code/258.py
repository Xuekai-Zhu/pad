def solution():
    s = "Julia Kirsten Pam Adan"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())