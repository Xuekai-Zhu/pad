def solution():
    s = "Penny Harry Jessica Horacio"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())