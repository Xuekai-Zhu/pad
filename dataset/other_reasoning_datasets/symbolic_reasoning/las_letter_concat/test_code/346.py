def solution():
    s = "Paris Jimmie Andrew Ramón"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())