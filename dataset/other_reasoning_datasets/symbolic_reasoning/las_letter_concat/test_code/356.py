def solution():
    s = "Russell Mitchell Bee Faith"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())