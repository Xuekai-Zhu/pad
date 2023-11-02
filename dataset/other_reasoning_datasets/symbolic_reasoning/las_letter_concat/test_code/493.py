def solution():
    s = "Len Marquis Kylie Sandra"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())