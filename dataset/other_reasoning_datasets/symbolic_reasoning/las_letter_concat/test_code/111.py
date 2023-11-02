def solution():
    s = "Jesús Vidal Maxine Gloria"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())