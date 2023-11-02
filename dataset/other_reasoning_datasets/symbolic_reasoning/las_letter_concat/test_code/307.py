def solution():
    s = "Angeles Richard Luciana Darlene"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())