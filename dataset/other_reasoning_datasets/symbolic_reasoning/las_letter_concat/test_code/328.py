def solution():
    s = "Darwin Colin Cj Abhishek"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())