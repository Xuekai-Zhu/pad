def solution():
    s = "Jody Juan Rebekah Kaylee"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())