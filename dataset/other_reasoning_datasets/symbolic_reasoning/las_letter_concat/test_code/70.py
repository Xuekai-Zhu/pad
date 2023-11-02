def solution():
    s = "Michele Karan Abraham Ellen"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())