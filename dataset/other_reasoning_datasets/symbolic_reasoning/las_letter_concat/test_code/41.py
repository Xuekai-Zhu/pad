def solution():
    s = "Gavin Neha Asha Baltazar"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())