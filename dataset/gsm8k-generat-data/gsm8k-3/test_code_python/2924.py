def solution():
    """Madeline has 10 flowers. If 4 flowers are red, 2 flowers are white, and the rest are blue, what percentage of flowers are blue?"""
    # Define the number of red, white, and blue flowers
    red = 4
    white = 2
    blue = 10 - red - white

    # Calculate the percentage of blue flowers
    blue_percentage = (blue / 10) * 100

    # Display the percentage of blue flowers
    result = blue_percentage
    return result

print(solution())