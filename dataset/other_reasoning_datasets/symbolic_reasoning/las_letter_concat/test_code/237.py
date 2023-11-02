def solution():
    s = "Yajaira Terrell Adam Lexie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())