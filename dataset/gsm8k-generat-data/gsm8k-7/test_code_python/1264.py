def solution():
    width = 21  # in inches
    height = 12  # in inches
    dpi = 100  # dots per inch

    # Calculate the total number of pixels
    total_pixels = width * dpi * height * dpi
    result = total_pixels
    return result

print(solution())