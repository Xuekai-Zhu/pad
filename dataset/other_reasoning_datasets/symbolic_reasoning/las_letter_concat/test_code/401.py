def solution():
    s = "Blanca Monika Ervin Lori"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())