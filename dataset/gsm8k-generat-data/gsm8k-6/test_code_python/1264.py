def solution():
    # Calculate the total number of pixels in the monitor
    width_inches = 21
    height_inches = 12
    dots_per_inch = 100
    total_pixels = width_inches * dots_per_inch * height_inches * dots_per_inch
    result = total_pixels
    return result

print(solution())