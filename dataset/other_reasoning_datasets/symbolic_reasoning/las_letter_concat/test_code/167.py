def solution():
    s = "Sunil Tiana Darla Darnell"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())