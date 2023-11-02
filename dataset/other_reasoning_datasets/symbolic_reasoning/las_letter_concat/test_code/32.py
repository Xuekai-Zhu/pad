def solution():
    s = "Phillip Ajay Janie Augusto"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())