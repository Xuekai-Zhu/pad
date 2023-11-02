def solution():
    s = "Karen Hector Mai Steven"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())