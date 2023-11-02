def solution():
    s = "Marty Justine Edgardo Osman"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())