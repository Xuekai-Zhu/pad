def solution():
    """Stephanie is planning dinners to cook for the week and needs to figure out how much of each ingredient she should buy at the grocery store. She is making three recipes that call for lower sodium soy sauce as a main ingredient. One bottle of lower sodium soy sauce holds 16 ounces. There are 8 ounces in 1 cup. The first recipe Stephanie is going to cook calls for 2 cups of lower sodium soy sauce. The second recipe calls for 1 cup. The third recipe calls for 3 cups. If Stephanie can only buy 1 whole bottle of soy sauce no matter how much she needs exactly, how many bottles of lower sodium soy sauce should Stephanie buy to allow for all three recipes?"""
    # Calculate the total amount of soy sauce needed in cups
    total_soy_sauce_cups = 2 + 1 + 3

    # Convert the total amount to ounces
    total_soy_sauce_ounces = total_soy_sauce_cups * 8

    # Calculate the number of bottles needed, rounding up to ensure enough soy sauce is purchased
    bottles_needed = math.ceil(total_soy_sauce_ounces / 16)

    result = bottles_needed
    return result

print(solution())