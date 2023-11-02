def solution():
    s = "Kristie Johnnie Marisa Derick"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())