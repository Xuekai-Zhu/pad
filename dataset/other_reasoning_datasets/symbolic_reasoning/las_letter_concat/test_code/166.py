def solution():
    s = "Anand Estefania Stanley Lizette"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())