def solution():
    s = "Angela Krista Cora Denisse"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())