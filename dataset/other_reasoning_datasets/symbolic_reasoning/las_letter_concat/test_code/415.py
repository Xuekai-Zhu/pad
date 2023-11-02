def solution():
    s = "Seth Dario Anne Jodie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())