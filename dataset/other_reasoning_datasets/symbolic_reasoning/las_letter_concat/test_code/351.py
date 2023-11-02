def solution():
    s = "Skyler Oliver Cristy Sierra"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())