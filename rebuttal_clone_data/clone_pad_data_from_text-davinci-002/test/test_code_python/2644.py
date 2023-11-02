def solution():
    wireless_mice = 0.5
    optical_mice = 0.25
    total_mice = 1
    trackball_mice = total_mice - wireless_mice - optical_mice
    result = trackball_mice * 80
    return result

print(solution())