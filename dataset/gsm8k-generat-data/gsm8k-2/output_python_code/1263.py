def solution():
    """A monitor is 21 inches by 12 inches. There are 100 dots per inch. How many total pixels are there?"""
    width_inches = 21
    height_inches = 12
    dpi = 100
    total_width_pixels = width_inches * dpi
    total_height_pixels = height_inches * dpi
    total_pixels = total_width_pixels * total_height_pixels
    result = total_pixels
    return result

print(solution())