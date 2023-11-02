def solution():
    s = "Tomas Nic Zoila Calvin"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())