def solution():
    """To make a lasagna Martha needs 1.5kg of cheese and 500 grams of meat. The cheese costs $6 per kilogram, and the meat $8 per kilogram. How much does Martha need to pay for the ingredients?"""
    # Define the prices and quantities of cheese and meat
    cheese_price_per_kg = 6
    cheese_quantity = 1.5
    meat_price_per_kg = 8
    meat_quantity = 0.5

    # Calculate the total cost of cheese and meat
    cheese_cost = cheese_price_per_kg * cheese_quantity
    meat_cost = meat_price_per_kg * meat_quantity
    total_cost = cheese_cost + meat_cost

    # return the result
    result = total_cost
    return result

print(solution())