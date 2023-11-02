def solution():
    s = "Neil Dani Eddie Marcelino"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())