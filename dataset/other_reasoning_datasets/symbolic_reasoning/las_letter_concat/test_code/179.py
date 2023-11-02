def solution():
    s = "Debi Raymond Luis Federico"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())