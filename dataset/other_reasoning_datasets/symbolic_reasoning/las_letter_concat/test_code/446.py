def solution():
    s = "Courtney Ann John Fer"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())