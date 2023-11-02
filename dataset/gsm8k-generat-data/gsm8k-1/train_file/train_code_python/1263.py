def solution():
    """A monitor is 21 inches by 12 inches. There are 100 dots per inch. How many total pixels are there?"""
    monitor_width = 21
    monitor_height = 12
    dots_per_inch = 100
    total_pixels = monitor_width * dots_per_inch * monitor_height * dots_per_inch
    result = total_pixels
    return result

print(solution())