def solution():
    s = "Marc Doris Ernie Gary"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())