def solution():
    s = "Amanda Geoff Belinda Gaurav"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())