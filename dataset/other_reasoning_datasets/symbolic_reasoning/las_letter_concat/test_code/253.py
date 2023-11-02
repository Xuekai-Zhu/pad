def solution():
    s = "Jim Dwayne Ricky Artemio"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())