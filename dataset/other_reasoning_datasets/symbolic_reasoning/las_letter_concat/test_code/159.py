def solution():
    s = "Franklin Rochelle Brent Sarai"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())