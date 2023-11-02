def solution():
    s = "Bob Aman Richie Sana"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())