def solution():
    s = "Sophie Gregorio Avery Pooja"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())