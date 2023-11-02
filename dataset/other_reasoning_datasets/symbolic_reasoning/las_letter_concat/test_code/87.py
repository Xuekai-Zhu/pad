def solution():
    s = "Sally Sadie Christie Ellie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())