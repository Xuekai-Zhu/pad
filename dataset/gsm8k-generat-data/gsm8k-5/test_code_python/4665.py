def solution():
    total_mice = 80  # Marky's shop sold a total of 80 mice
    wireless_mice = total_mice/2  # Half of the sales are wireless mice
    optical_mice = total_mice/4  # One-fourth of the sales are optical mice
    trackball_mice = total_mice - wireless_mice - optical_mice  # The remaining mice are trackball mice
    result = trackball_mice
    return result

print(solution())