def solution():
    s = "Trish Vero Victor Clemente"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())