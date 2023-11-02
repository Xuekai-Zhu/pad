def solution():
    total_mice = 80
    wireless_mice = total_mice / 2
    optical_mice = total_mice / 4
    trackball_mice = total_mice - wireless_mice - optical_mice
    result = trackball_mice
    return result

print(solution())