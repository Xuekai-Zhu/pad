def solution():
    """Marky owns a computer accessory shop. For this month, half of their sales are wireless mice, one-fourth are optical mice, and the rest are trackball mice. If Marky's shop was able to sell a total of 80 mice, how many of them are trackball mice?"""
    total_mice = 80
    wireless_mice = total_mice / 2
    optical_mice = total_mice / 4
    trackball_mice = total_mice - wireless_mice - optical_mice
    result = trackball_mice
    return result

print(solution())