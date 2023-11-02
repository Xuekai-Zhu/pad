def solution():
    s = "Ashish Tracey Varun Emil"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())