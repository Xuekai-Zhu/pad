def solution():
    s = "Ralph Jeanne Kyle Alejandro"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())