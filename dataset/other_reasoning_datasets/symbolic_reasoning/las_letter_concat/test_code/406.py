def solution():
    s = "Justin Neal Jt Lucia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())