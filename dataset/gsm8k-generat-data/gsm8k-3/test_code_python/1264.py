def solution():
    """A monitor is 21 inches by 12 inches.  There are 100 dots per inch.  How many total pixels are there?"""
    # Define the dimensions of the monitor in inches
    WIDTH = 21
    HEIGHT = 12

    # Define the number of dots per inch
    DPI = 100

    # Calculate the total number of pixels
    total_pixels = WIDTH * DPI * HEIGHT * DPI

    # Display the total number of pixels
    result = total_pixels
    return result

print(solution())