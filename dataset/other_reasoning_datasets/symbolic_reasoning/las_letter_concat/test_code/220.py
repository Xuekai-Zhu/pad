def solution():
    s = "Kendall Matias Kaleb Randy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())