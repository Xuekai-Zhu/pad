def solution():
    """Nina made a two-layer cake and a dozen cupcakes for her friend’s birthday party. Each layer of cake takes the same amount of sugar to make as a dozen cupcakes. Nina used 720 grams of sugar to bake everything. How many grams of sugar are in one cupcake?"""
    sugar_per_cake_layer = 720 / 3
    sugar_per_cupcake = sugar_per_cake_layer / 12
    result = sugar_per_cupcake
    return result

print(solution())