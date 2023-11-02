def solution():
    # Calculate the total number of mushroom pieces
    total_pieces = 38 + 42 + 8  # sum of mushroom pieces on Kenny's, Karla's pizzas and remaining on the cutting board
    # Since each mushroom was cut into 4 pieces, find the total number of mushrooms
    total_mushrooms = total_pieces / 4
    result = total_mushrooms
    return result

print(solution())