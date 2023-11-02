def solution():
    s = "Les Jun Noe Juliana"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())