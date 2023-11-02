def solution():
    s = "Idalia Arnoldo Marla Duane"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())