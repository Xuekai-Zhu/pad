def solution():
    """Thomas is making hummus. One of the ingredients in a hummus recipe is chickpeas. For one serving of hummus, the recipe calls for 1 cup of chickpeas. In a can of chickpeas, there are 16 ounces of chickpeas. In one cup of chickpeas, there are 6 ounces. To make 20 servings, how many cans of chickpeas should Thomas buy?"""
    ounces_per_serving = 6
    ounces_per_can = 16
    servings_per_can = ounces_per_can // ounces_per_serving
    total_servings = 20
    cans_needed = (total_servings + servings_per_can - 1) // servings_per_can
    result = cans_needed
    return result

print(solution())