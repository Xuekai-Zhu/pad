def solution():
    # Calculate the total number of mushroom pieces sprinkled on the pizzas
    total_pieces_on_pizzas = 38 + 42

    # Calculate the total number of mushroom pieces before sprinkling on the pizzas
    total_pieces_before = total_pieces_on_pizzas + 8

    # Calculate the total number of mushrooms cut up at the beginning
    total_mushrooms = total_pieces_before / 4
    result = total_mushrooms
    return result

print(solution())