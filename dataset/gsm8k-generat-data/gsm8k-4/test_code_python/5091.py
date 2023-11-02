def solution():
    """Paul uses 1 can of frosting to frost a layer cake. He uses a half can of frosting for a single cake, or a single pan of brownies, or a dozen cupcakes. For Saturday, he needs to have 3 layer cakes, 6 dozen cupcakes, 12 single cakes, and 18 pans of brownies ready and frosted for customer pick up. How many cans of frosting will he need?"""
    # Define the amount of frosting needed for each type of dessert
    frosting_per_cake = 1
    frosting_per_single_cake = 0.5
    frosting_per_brownie = 0.5
    frosting_per_dozen_cupcakes = 0.5

    # Calculate the total amount of frosting needed
    total_frosting_needed = (frosting_per_cake * 3) + (frosting_per_single_cake * 12) + (frosting_per_brownie * 18) + (frosting_per_dozen_cupcakes * 6)

    # Round up to the nearest whole can of frosting
    cans_of_frosting = int(total_frosting_needed + 0.5)

    # return the result
    result = cans_of_frosting
    return result

print(solution())