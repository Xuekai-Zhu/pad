def solution():
    s = "Cruz Wilber Marilu Malik"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())