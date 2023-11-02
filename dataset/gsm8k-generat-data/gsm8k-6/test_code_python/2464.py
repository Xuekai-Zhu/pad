def solution():
    # Calculate the total amount of water needed for the bubble mix
    total_water = 40 / 8  # the container can hold 40 ounces of liquid, and there are 8 ounces in a cup of water

    # Calculate the total amount of soap needed for the bubble mix
    total_soap = 3 * total_water  # the recipe calls for 3 tablespoons of soap for every 1 cup of water

    result = total_soap
    return result

print(solution())