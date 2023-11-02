def solution():
    """Jackson is laying tile in a courtyard that measures 10 feet by 25 feet. He needs 4 tiles per square foot of space. 40% of the tiles are green marble that costs $3/tile, and the rest are red tile that costs $1.50/tile. How much does he pay total for tile?"""
    # Calculate the total square footage of the courtyard
    square_footage = 10 * 25

    # Calculate the total number of tiles needed
    total_tiles = square_footage * 4

    # Calculate the number of green marble tiles needed
    green_tiles = int(total_tiles * 0.4)

    # Calculate the number of red tiles needed
    red_tiles = total_tiles - green_tiles

    # Calculate the total cost of the green marble tiles
    green_cost = green_tiles * 3

    # Calculate the total cost of the red tiles
    red_cost = red_tiles * 1.5

    # Calculate the total cost of all the tiles
    total_cost = green_cost + red_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())