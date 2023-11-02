def solution():
    s = "Lorraine Corinne Kate Floyd"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())