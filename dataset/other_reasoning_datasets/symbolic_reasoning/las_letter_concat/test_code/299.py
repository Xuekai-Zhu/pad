def solution():
    s = "Nery Cindy Jess Chris"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())