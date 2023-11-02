def solution():
    num_layers = 2
    num_cupcakes = 12
    total_sugar = 720

    # Calculate the amount of sugar needed for one layer of cake
    sugar_per_layer = total_sugar / (num_layers + num_cupcakes)

    # Calculate the amount of sugar needed for one cupcake
    sugar_per_cupcake = sugar_per_layer / num_cupcakes
    result = sugar_per_cupcake
    return result

print(solution())