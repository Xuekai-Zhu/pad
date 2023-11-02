def solution():
    s = "Felipe Heidi Nino Bradley"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())