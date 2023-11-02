def solution():
    s = "Walter Mikayla Larry Ryan"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())