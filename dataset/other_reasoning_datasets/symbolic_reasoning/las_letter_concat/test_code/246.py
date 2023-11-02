def solution():
    s = "Ever Gio Elia Ramesh"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())