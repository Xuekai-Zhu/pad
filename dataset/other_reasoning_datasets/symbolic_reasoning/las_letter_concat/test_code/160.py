def solution():
    s = "Clinton Yanira Barbara Betsy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())