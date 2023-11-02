def solution():
    s = "Clark Jenn Diane Blair"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())