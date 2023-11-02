def solution():
    s = "Luz Terence Elder Jazmin"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())