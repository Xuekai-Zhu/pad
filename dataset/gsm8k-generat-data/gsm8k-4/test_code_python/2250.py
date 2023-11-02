def solution():
    """Thomas is making hummus. One of the ingredients in a hummus recipe is chickpeas. For one serving of hummus, the recipe calls for 1 cup of chickpeas. In a can of chickpeas, there are 16 ounces of chickpeas. In one cup of chickpeas, there are 6 ounces. To make 20 servings, how many cans of chickpeas should Thomas buy?"""
    # Define the amount of chickpeas needed for one serving and for 20 servings
    chickpeas_per_serving = 1  # 1 cup
    chickpeas_for_20_servings = 20 * chickpeas_per_serving 

    # Calculate the amount of chickpeas in ounces needed for 20 servings
    chickpeas_in_ounces = chickpeas_for_20_servings * 6

    # Calculate the number of cans needed, rounding up to the nearest whole can
    cans_needed = math.ceil(chickpeas_in_ounces / 16)

    # Return the result
    result = cans_needed
    return result

print(solution())