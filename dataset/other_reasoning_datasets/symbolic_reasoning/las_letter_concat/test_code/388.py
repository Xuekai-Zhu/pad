def solution():
    s = "Malcolm Hussein Franco Hugo"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())