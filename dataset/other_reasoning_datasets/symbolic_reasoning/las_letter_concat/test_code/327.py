def solution():
    s = "Andy Cecilia Gretchen Sandi"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())