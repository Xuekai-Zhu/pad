def solution():
    s = "April Molly Maurice Jaclyn"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())