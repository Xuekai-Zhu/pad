def solution():
    s = "Liliana Quincy Bart Makayla"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())