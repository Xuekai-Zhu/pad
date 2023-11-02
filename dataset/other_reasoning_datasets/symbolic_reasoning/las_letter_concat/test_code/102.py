def solution():
    s = "Manolo Bobbie Ash Jaqueline"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())