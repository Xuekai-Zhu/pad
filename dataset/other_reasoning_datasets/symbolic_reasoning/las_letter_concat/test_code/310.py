def solution():
    s = "Guille Lisa Harvey Gina"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())