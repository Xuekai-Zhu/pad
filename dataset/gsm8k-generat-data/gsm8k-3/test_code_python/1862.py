def solution():
    """Jason bought 4 dozen cupcakes. He plans to give 3 cupcakes each to his cousins. How many cousins does Jason have?"""
    # Define the number of cupcakes Jason bought and the number he plans to give to each cousin
    cupcakes = 4 * 12
    cupcakes_per_cousin = 3

    # Calculate the number of cousins Jason has
    cousins = cupcakes // cupcakes_per_cousin

    # Display the number of cousins
    result = cousins
    return result

print(solution())