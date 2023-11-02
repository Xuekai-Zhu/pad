def solution():
    s = "Wilson Abbey Harold Nelly"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())