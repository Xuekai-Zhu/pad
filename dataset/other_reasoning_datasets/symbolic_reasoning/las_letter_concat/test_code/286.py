def solution():
    s = "Claudia Cole Matthew Juan Pablo"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())