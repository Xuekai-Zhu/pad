def solution():
    s = "Erwin Chad Margarito Shanna"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())