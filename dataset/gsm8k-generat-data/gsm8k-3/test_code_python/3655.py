def solution():
    """To make a lasagna Martha needs 1.5kg of cheese and 500 grams of meat. The cheese costs $6 per kilogram, and the meat $8 per kilogram. How much does Martha need to pay for the ingredients?"""
    # Define the amount of each ingredient needed
    cheese_kg = 1.5
    meat_kg = 0.5

    # Define the cost per kilogram of each ingredient
    cheese_cost_per_kg = 6
    meat_cost_per_kg = 8

    # Calculate the total cost of the cheese
    cheese_cost = cheese_kg * cheese_cost_per_kg

    # Calculate the total cost of the meat
    meat_cost = meat_kg * meat_cost_per_kg

    # Calculate the total cost of all the ingredients
    total_cost = cheese_cost + meat_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())