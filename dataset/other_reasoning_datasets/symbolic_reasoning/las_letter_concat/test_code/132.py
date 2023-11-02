def solution():
    s = "Daniella Dianne Ram Mirian"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())