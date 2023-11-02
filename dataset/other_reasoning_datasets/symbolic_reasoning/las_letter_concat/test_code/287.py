def solution():
    s = "Arturo Dominick Christa Myles"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())