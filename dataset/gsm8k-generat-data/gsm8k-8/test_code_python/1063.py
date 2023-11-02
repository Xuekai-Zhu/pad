def solution():
    # Define the amount of sugar used for each layer of cake and each cupcake
    sugar_per_cake_layer = 1 * 12  # one dozen cupcakes for one cake layer
    sugar_per_cupcake = 1

    # Calculate the total amount of cupcakes and cake layers baked
    total_cupcakes = 12
    total_cake_layers = 2

    # Calculate the total amount of sugar used
    total_sugar_used = 720

    # Calculate the amount of sugar in one cupcake
    sugar_per_cupcake = (total_sugar_used - (sugar_per_cake_layer * total_cake_layers)) / total_cupcakes

    result = sugar_per_cupcake
    return result

print(solution())