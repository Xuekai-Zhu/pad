def solution():
    s = "Alonzo Dorothy Alfred Rodriguez"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())