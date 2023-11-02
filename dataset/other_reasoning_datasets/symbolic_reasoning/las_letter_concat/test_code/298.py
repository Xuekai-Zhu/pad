def solution():
    s = "Bethany Rakesh Christine Dinesh"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())