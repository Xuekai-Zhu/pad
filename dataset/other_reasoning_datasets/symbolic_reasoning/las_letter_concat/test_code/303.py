def solution():
    s = "Lore Erasmo Louis David"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())