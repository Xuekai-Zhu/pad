def solution():
    s = "Sonia Griffin Claude Josephine"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())