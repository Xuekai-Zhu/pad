def solution():
    s = "Prince Rene Vishal Patrick"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())