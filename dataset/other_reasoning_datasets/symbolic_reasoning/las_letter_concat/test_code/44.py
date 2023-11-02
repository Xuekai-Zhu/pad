def solution():
    s = "Meg Andrey Gerard Lilia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())