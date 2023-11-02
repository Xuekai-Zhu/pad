def solution():
    s = "Margarita Anabel Shaun Celina"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())