def solution():
    s = "Hayden Maya Zack Roberto"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())