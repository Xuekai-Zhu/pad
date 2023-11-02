def solution():
    s = "Todd Joni Gil Fran"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())