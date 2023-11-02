def solution():
    """Madeline has 10 flowers. If 4 flowers are red, 2 flowers are white, and the rest are blue, what percentage of flowers are blue?"""
    # Define the initial number of flowers
    total_flowers = 10

    # Calculate the number of red flowers
    red_flowers = 4

    # Calculate the number of white flowers
    white_flowers = 2

    # Calculate the number of blue flowers
    blue_flowers = total_flowers - red_flowers - white_flowers

    # Calculate the percentage of blue flowers
    blue_percentage = (blue_flowers / total_flowers) * 100

    # return the result
    result = blue_percentage
    return result

print(solution())