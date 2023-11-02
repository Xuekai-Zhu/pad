def solution():
    # Calculate the frosting needed for layer cakes
    frosting_for_layer_cakes = 1 * 3

    # Calculate the frosting needed for single cakes
    frosting_for_single_cakes = 0.5 * 12

    # Calculate the frosting needed for pans of brownies
    frosting_for_brownies = 0.5 * 18

    # Calculate the frosting needed for cupcakes
    frosting_for_cupcakes = 0.5 * 6 * 12

    # Calculate the total frosting needed
    total_frosting = frosting_for_layer_cakes + frosting_for_single_cakes + frosting_for_brownies + frosting_for_cupcakes

    result = total_frosting
    return result

print(solution())