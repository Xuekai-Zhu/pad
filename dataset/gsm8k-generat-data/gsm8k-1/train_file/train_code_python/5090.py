def solution():
    """Paul uses 1 can of frosting to frost a layer cake. He uses a half can of frosting for a single cake, or a single pan of brownies, or a dozen cupcakes. For Saturday, he needs to have 3 layer cakes, 6 dozen cupcakes, 12 single cakes and 18 pans of brownies ready and frosted for customer pick up. How many cans of frosting will he need?"""
    frosting_for_layer_cake = 1
    frosting_for_single_cake_or_brownie_or_cupcake = 0.5
    total_frosting_needed = frosting_for_layer_cake * 3 + \
        frosting_for_single_cake_or_brownie_or_cupcake * \
        (6 + 12 + 18)
    result = total_frosting_needed
    return result

print(solution())