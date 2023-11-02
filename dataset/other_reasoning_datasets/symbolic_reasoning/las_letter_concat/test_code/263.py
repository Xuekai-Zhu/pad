def solution():
    s = "Wilfredo Abby Karthik Perry"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())