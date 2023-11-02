def solution():
    s = "Anil Enrique Jimmy Jhonny"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())