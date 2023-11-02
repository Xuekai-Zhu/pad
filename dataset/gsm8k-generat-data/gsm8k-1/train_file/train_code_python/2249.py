def solution():
    """Thomas is making hummus. One of the ingredients in a hummus recipe is chickpeas. 
    For one serving of hummus, the recipe calls for 1 cup of chickpeas. 
    In a can of chickpeas, there are 16 ounces of chickpeas. In one cup of chickpeas, there are 6 ounces. 
    To make 20 servings, how many cans of chickpeas should Thomas buy?"""
    chickpeas_per_cup = 6
    ounces_per_can = 16
    chickpeas_per_can = ounces_per_can / chickpeas_per_cup
    servings = 20
    cans_needed = servings * chickpeas_per_cup / ounces_per_can
    result = cans_needed
    return result

print(solution())