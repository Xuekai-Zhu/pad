def solution():
    s = "Hailey Avi Bree Samira"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())