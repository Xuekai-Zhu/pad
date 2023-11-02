def solution():
    s = "Talia Nicki Tia Divya"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())