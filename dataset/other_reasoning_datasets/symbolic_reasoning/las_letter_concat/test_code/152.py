def solution():
    s = "Bernard Lidia Sebastian Judy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())