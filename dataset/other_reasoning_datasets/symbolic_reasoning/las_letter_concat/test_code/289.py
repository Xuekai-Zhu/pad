def solution():
    s = "Teresa Reid Karin Gracie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())