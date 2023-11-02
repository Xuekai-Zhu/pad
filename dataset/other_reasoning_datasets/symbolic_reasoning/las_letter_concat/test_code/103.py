def solution():
    s = "Jorge Luis Mo Alexia Jerry"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())