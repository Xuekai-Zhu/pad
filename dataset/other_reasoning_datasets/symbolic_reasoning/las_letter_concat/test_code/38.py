def solution():
    s = "Nubia Sarah Jalen Kris"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())