def solution():
    s = "Clayton Edison Debbie Elvira"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())