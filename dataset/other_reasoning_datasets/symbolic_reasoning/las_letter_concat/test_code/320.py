def solution():
    s = "Kristy Brandi Lizeth Petra"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())