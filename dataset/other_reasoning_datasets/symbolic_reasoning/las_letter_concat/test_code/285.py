def solution():
    s = "Vijay Sherrie Doug Suzy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())