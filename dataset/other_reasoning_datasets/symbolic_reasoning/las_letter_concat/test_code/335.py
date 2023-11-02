def solution():
    s = "Deanna Terri Gabriela Jonah"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())