def solution():
    s = "Dustin Luiz Rolando Connor"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())