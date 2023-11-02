def solution():
    s = "Katia Mina Cam Ronda"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())