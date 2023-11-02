def solution():
    s = "Ari Jasmine Elliot Kendrick"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())