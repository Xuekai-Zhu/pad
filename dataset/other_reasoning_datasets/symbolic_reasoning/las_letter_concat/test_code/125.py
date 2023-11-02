def solution():
    s = "Jordan Yoni Lawrence Aura"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())