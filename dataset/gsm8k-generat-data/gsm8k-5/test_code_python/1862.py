def solution():
    cupcakes = 4 * 12  # Jason bought 4 dozen cupcakes, which is equal to 48 cupcakes
    cupcakes_per_cousin = 3  # Jason plans to give 3 cupcakes to each cousin

    # Calculate the number of cousins Jason has
    num_cousins = cupcakes // cupcakes_per_cousin

    result = num_cousins
    return result

print(solution())