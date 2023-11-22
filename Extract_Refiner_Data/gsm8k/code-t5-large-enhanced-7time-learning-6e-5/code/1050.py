def solution():
    
    # Define the total area of the floor and the cost of each tile
    total_area = 200
    tile_cost = 12

    # Calculate the number of tiles needed to renovate the floor
    num_tiles = total_area / tile_cost

    # Calculate the total cost of the tiles
    total_cost = num_tiles * tile_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())