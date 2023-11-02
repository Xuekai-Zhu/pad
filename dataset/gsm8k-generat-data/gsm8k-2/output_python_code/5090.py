def solution():
    """Paul uses 1 can of frosting to frost a layer cake. He uses a half can of frosting for a single cake, or a single pan of brownies,
    or a dozen cupcakes. For Saturday, he needs to have 3 layer cakes, 6 dozen cupcakes, 12 single cakes and 18 pans of brownies ready
    and frosted for customer pick up. How many cans of frosting will he need?"""
    layer_cakes = 3
    single_cakes = 12
    pans_of_brownies = 18
    dozens_of_cupcakes = 6
    frosting_needed = layer_cakes + (single_cakes + pans_of_brownies + dozens_of_cupcakes * 0.5)
    result = frosting_needed
    return result

print(solution())