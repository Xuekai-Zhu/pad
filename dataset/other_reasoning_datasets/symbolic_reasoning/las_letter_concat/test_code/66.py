def solution():
    s = "Lorena Shana Priscilla Summer"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())