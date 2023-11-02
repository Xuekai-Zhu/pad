def solution():
    s = "Roni Nikita Hannah Kiana"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())