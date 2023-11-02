def solution():
    """A monitor is 21 inches by 12 inches. There are 100 dots per inch. How many total pixels are there?"""
    # Define the dimensions of the monitor in inches
    width = 21
    height = 12

    # Define the number of dots per inch
    dpi = 100

    # Calculate the total number of pixels
    pixels = width * dpi * height * dpi

    # Return the result
    result = pixels
    return result

print(solution())