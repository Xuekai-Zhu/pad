def solution():
    """Mary is building a mosaic for her school cafeteria's wall. It will be 10 feet tall and 15 feet long. Each tile she uses is 1 inch square. How many tiles will she need?"""
    # Define the dimensions of the mosaic in feet
    height_feet = 10
    length_feet = 15

    # Convert the dimensions to inches
    height_inches = height_feet * 12
    length_inches = length_feet * 12

    # Calculate the total number of tiles needed
    total_tiles = height_inches * length_inches

    # Display the result
    result = total_tiles
    return result

print(solution())