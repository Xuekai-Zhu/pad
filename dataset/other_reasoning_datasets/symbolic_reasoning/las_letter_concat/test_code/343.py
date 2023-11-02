def solution():
    s = "Nicolas Aaliyah Pascual Rob"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())