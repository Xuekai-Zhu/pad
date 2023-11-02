def solution():
    s = "Meagan Naomi Israel Marie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())