def solution():
    s = "Kristi Eduardo Angelo Clare"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())