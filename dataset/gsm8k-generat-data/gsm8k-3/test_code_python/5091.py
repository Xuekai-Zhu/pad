def solution():
    """Paul uses 1 can of frosting to frost a layer cake. He uses a half can of frosting for a single cake, or a single pan of brownies, or a dozen cupcakes. For Saturday, he needs to have 3 layer cakes, 6 dozen cupcakes, 12 single cakes and 18 pans of brownies ready and frosted for customer pick up. How many cans of frosting will he need?"""
    # Define the amount of frosting needed for each item
    FROSTING_PER_LAYER_CAKE = 1
    FROSTING_PER_SINGLE_CAKE = 0.5
    FROSTING_PER_BROWNIE = 0.5
    FROSTING_PER_CUPCAKE = 0.5 / 12

    # Calculate the total amount of frosting needed
    total_frosting = (FROSTING_PER_LAYER_CAKE * 3) + (FROSTING_PER_SINGLE_CAKE * 12) + (FROSTING_PER_BROWNIE * 18) + (FROSTING_PER_CUPCAKE * 6)

    # Display the total amount of frosting needed
    result = total_frosting
    return result

print(solution())