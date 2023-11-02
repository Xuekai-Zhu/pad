def solution():
    s = "Jr Meredith Zoe Robby"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())