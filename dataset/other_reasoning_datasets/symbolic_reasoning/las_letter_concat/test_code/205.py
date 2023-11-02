def solution():
    s = "Forrest Juanito Allan Candice"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())