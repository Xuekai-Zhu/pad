def solution():
    s = "Carlitos Damaris Nikhil Jennie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())