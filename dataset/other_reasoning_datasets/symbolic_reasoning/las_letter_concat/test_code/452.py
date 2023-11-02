def solution():
    s = "Christina Edna Ileana Lynette"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())