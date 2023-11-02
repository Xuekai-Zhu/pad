def solution():
    s = "Diego Val Vincent Stacie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())