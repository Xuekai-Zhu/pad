def solution():
    """Marky owns a computer accessory shop. For this month, half of their sales are wireless mice, one-fourth are optical mice, and the rest are trackball mice. If Marky's shop was able to sell a total of 80 mice, how many of them are trackball mice?"""
    # Define the percentages of each type of mouse sold
    WIRELESS_PERCENT = 0.5
    OPTICAL_PERCENT = 0.25

    # Calculate the number of wireless mice sold
    wireless_mice = round(WIRELESS_PERCENT * 80)

    # Calculate the number of optical mice sold
    optical_mice = round(OPTICAL_PERCENT * 80)

    # Calculate the number of trackball mice sold
    trackball_mice = 80 - wireless_mice - optical_mice

    # Display the number of trackball mice sold
    result = trackball_mice
    return result

print(solution())