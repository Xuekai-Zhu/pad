def solution():
    s = "Otto Marjorie Leonor Esther"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())