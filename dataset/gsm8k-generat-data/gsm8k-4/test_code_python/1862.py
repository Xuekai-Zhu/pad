def solution():
    """Jason bought 4 dozen cupcakes. He plans to give 3 cupcakes each to his cousins. How many cousins does Jason have?"""
    # Define the number of cupcakes bought
    cupcakes_bought = 4 * 12

    # Define the number of cupcakes given per cousin
    cupcakes_per_cousin = 3

    # Calculate the number of cousins
    cousins = cupcakes_bought / cupcakes_per_cousin

    # Return the result
    result = cousins
    return result

print(solution())