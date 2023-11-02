def solution():
    """Nina made a two-layer cake and a dozen cupcakes for her friend’s birthday party. Each layer of cake takes the same amount of sugar to make as a dozen cupcakes. Nina used 720 grams of sugar to bake everything. How many grams of sugar are in one cupcake?"""
    # Define the amount of sugar in one layer of cake
    CAKE_SUGAR = 12

    # Define the total number of cupcakes and layers of cake
    cupcakes = 12
    layers = 2

    # Define the total amount of sugar used
    total_sugar = 720

    # Calculate the amount of sugar in one cupcake
    cake_sugar = CAKE_SUGAR * layers
    total_cupcakes = cupcakes * layers
    total_cake_sugar = cake_sugar * layers
    cupcake_sugar = (total_sugar - total_cake_sugar) / total_cupcakes

    # Display the amount of sugar in one cupcake
    result = cupcake_sugar
    return result

print(solution())