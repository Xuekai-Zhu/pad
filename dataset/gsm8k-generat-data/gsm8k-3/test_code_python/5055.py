def solution():
    """Blinky wants to make a three-layer birthday cake for her mom. The recipe for the smallest layer of the cake requires 2 cups of sugar. If the second layer is twice as big as the first and the third layer is three times larger than the second, how many total cups of sugar will she need for the third layer?"""
    
    # Define the sugar required for the smallest layer
    smallest_layer_sugar = 2

    # Define the size ratio for the layers
    second_layer_ratio = 2
    third_layer_ratio = 3

    # Calculate the sugar required for the second layer
    second_layer_sugar = smallest_layer_sugar * second_layer_ratio

    # Calculate the sugar required for the third layer
    third_layer_sugar = second_layer_sugar * third_layer_ratio

    # Calculate the total sugar required for the cake
    total_sugar = smallest_layer_sugar + second_layer_sugar + third_layer_sugar

    # Display the total sugar required for the third layer
    result = third_layer_sugar
    return result

print(solution())