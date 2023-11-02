def solution():
    # Calculate the number of wireless and optical mice sold
    wireless_mice = 80 * 0.5
    optical_mice = 80 * 0.25

    # Calculate the number of trackball mice sold
    trackball_mice = 80 - wireless_mice - optical_mice
    result = trackball_mice
    return result

print(solution())