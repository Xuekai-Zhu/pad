def solution():
    s = "Rich Parker Edward Milagros"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())