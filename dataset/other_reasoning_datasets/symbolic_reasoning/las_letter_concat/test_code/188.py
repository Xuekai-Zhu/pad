def solution():
    s = "Peggy Trent Darrell Pamela"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())