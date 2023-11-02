def solution():
    s = "Mia Art Samantha Lety"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())