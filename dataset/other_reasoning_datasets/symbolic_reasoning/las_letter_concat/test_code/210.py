def solution():
    s = "Deon Lane Everett Lindsay"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())