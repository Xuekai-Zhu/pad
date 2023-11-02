def solution():
    s = "Pretty Jada Sarita Allen"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())