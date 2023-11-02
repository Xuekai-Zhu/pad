def solution():
    s = "Sherri Genesis Jeffrey Samir"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())