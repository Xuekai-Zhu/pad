def solution():
    s = "Oscar George Sanjay Haydee"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())