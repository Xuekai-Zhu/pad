def solution():
    """Nina made a two-layer cake and a dozen cupcakes for her friend’s birthday party. Each layer of cake takes the same amount of sugar to make as a dozen cupcakes. Nina used 720 grams of sugar to bake everything. How many grams of sugar are in one cupcake?"""
    # Define the amount of sugar used for one layer of cake
    sugar_per_layer = None

    # Define the amount of sugar used for one cupcake
    sugar_per_cupcake = None

    # Define the total number of cupcakes
    total_cupcakes = 12

    # Define the total amount of sugar used
    total_sugar = 720

    # Calculate the amount of sugar used for one layer of cake
    sugar_per_layer = total_sugar / 3

    # Calculate the amount of sugar used for one cupcake
    sugar_per_cupcake = sugar_per_layer / total_cupcakes

    # Return the result
    result = sugar_per_cupcake
    return result

print(solution())