def solution():
    s = "Maria Elena Dewayne Mj Elliott"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())