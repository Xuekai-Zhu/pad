def solution():
    """Marky owns a computer accessory shop. For this month, half of their sales are wireless mice, one-fourth are optical mice, and the rest are trackball mice. If Marky's shop was able to sell a total of 80 mice, how many of them are trackball mice?"""
    total_sales = 80
    wireless_sales = total_sales / 2
    optical_sales = total_sales / 4
    trackball_sales = total_sales - wireless_sales - optical_sales
    result = trackball_sales
    return result

print(solution())