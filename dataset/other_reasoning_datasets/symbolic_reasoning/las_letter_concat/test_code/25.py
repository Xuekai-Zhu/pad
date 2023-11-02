def solution():
    s = "Rena Devon Rosalinda Paulina"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())