def solution():
    s = "Arnold Aidan Ally Ami"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())