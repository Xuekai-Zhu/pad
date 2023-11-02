def solution():
    s = "Kristopher Deb Jake Tammy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())