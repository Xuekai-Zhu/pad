def solution():
    s = "Marshall Herman Faye Grant"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())