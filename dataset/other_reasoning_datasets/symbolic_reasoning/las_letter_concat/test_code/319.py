def solution():
    s = "Logan Ely Abbie Colleen"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())