def solution():
    s = "Reginald Franky Kira Gordon"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())