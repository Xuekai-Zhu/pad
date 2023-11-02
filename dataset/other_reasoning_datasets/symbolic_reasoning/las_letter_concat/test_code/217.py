def solution():
    s = "Efrain Rickey Jonathan Kelli"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())