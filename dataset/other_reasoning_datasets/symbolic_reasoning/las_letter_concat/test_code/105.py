def solution():
    s = "Nabil Marlene Wendy Jillian"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())