def solution():
    """Thomas is making hummus. One of the ingredients in a hummus recipe is chickpeas. For one serving of hummus, the recipe calls for 1 cup of chickpeas. In a can of chickpeas, there are 16 ounces of chickpeas. In one cup of chickpeas, there are 6 ounces. To make 20 servings, how many cans of chickpeas should Thomas buy?"""
    # Calculate the total number of ounces of chickpeas needed
    ounces_needed = 20 * 1 * 6

    # Calculate the number of cans needed
    cans_needed = math.ceil(ounces_needed / 16)

    # Display the number of cans needed
    result = cans_needed
    return result

print(solution())