def solution():
    s = "Ernest Yuri Camila Ashlee"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())