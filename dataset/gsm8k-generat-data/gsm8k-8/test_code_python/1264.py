def solution():
    # Calculate the total number of pixels by multiplying the number of dots per inch by the area of the monitor in inches
    dots_per_inch = 100
    width_inches = 21
    height_inches = 12
    total_pixels = dots_per_inch * width_inches * dots_per_inch * height_inches
    result = total_pixels
    return result

print(solution())