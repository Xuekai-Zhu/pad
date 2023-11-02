def solution():
    s = "Juliet Ricardo Tita Dianna"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())