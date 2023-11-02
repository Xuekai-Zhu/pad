def solution():
    s = "Vinny Landon Miguel Caitlyn"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())