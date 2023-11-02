def solution():
    s = "Elizabeth Mitch Brooke Jordyn"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())