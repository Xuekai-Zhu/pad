def solution():
    s = "Tristan Marleny Santiago Viviana"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())