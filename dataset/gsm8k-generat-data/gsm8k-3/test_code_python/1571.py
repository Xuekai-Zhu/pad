def solution():
    """Mary is building a mosaic for her school cafeteria's wall. It will be 10 feet tall and 15 feet long. Each tile she uses is 1 inch square. How many tiles will she need?"""
    # Convert the dimensions to inches
    height = 10 * 12
    length = 15 * 12

    # Calculate the total area in square inches
    area = height * length

    # Calculate the number of tiles needed
    tiles = area / 1

    # Display the number of tiles
    result = tiles
    return result

print(solution())