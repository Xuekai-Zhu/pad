def solution():
    """Nina made a two-layer cake and a dozen cupcakes for her friend’s birthday party. Each layer of cake takes the same amount of sugar to make as a dozen cupcakes. Nina used 720 grams of sugar to bake everything. How many grams of sugar are in one cupcake?"""
    total_cupcakes = 12
    cake_layers = 2
    sugar_per_cake_layer = total_cupcakes
    total_sugar_used = 720
    sugar_per_cupcake = (total_sugar_used - (sugar_per_cake_layer * cake_layers)) / total_cupcakes
    result = sugar_per_cupcake
    return result

print(solution())