def solution():
    """Marky owns a computer accessory shop. For this month, half of their sales are wireless mice, one-fourth are optical mice, and the rest are trackball mice. If Marky's shop was able to sell a total of 80 mice, how many of them are trackball mice?"""
    # Define the total number of mice sold
    total_mice = 80

    # Calculate the number of wireless mice sold
    wireless_mice = total_mice / 2

    # Calculate the number of optical mice sold
    optical_mice = total_mice / 4

    # Calculate the number of trackball mice sold
    trackball_mice = total_mice - wireless_mice - optical_mice

    # return the result
    result = trackball_mice
    return result

print(solution())