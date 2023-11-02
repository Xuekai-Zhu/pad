def solution():
    # Calculate the total amount of frosting needed for each item
    frosting_per_cake = 1
    frosting_per_single_cake = 0.5
    frosting_per_pan_of_brownies = 0.5
    frosting_per_dozen_cupcakes = 0.5

    # Calculate the total amount of frosting needed for each item on Saturday
    total_frosting_cakes = frosting_per_cake * 3
    total_frosting_single_cakes = frosting_per_single_cake * 12
    total_frosting_pans_of_brownies = frosting_per_pan_of_brownies * 18
    total_frosting_cupcakes = frosting_per_dozen_cupcakes * 6

    # Calculate the total amount of frosting needed for Saturday
    total_frosting_needed = (total_frosting_cakes + total_frosting_single_cakes
                             + total_frosting_pans_of_brownies + total_frosting_cupcakes)

    # Calculate the number of cans of frosting needed
    cans_of_frosting_needed = total_frosting_needed / 1
    result = cans_of_frosting_needed
    return result

print(solution())