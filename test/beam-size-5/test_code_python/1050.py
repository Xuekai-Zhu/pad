def solution():
    total_area = 200  # The area of the kitchen floor is 200 SqFt
    tile_cost = 12  # Each tile costs $12
    tile_side_length = 1  # Each tile side is 1ft in length

    # Calculate the total length of the new square floor tiles
    total_tile_length = total_area * tile_side_length

    # Calculate the total cost of the new square floor tiles
    total_tile_cost = total_tile_length * tile_cost

    # Calculate the total cost of renovating the kitchen floor
    total_cost = total_area * total_tile_cost
    result = total_cost
    return result

print(solution())