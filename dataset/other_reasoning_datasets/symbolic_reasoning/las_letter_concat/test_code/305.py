def solution():
    s = "Wally Claire Helen Nacho"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())