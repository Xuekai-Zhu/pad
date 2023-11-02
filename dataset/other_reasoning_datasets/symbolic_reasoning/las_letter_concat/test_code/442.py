def solution():
    s = "Donald Lia Gonzalo Lily"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())