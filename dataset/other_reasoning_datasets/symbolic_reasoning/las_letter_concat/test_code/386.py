def solution():
    s = "Lara Greg Ethan Terrence"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())