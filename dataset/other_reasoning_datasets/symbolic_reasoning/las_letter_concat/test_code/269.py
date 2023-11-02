def solution():
    s = "Alexander Marina Valentina Mila"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())