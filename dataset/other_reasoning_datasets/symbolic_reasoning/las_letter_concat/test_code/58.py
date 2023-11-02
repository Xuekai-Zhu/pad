def solution():
    s = "Rubi Daisy Yadira Santa"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())