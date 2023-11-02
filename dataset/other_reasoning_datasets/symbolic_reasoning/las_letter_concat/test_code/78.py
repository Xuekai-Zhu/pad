def solution():
    s = "Lewis Azucena Kai Ravi"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())