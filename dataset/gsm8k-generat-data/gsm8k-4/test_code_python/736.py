def solution():
    """At the Delicious Delhi restaurant, Hilary bought three samosas at $2 each and four orders of pakoras, at $3 each, and a mango lassi, for $2. She left a 25% tip. How much did the meal cost Hilary, with tax, in dollars?"""
    # Define the prices of samosas, pakoras, and mango lassi
    samosa_price = 2
    pakora_price = 3
    lassi_price = 2

    # Calculate the cost of the food before tax and tip
    food_cost = (3 * samosa_price) + (4 * pakora_price) + lassi_price

    # Calculate the amount of the tip
    tip = 0.25 * food_cost

    # Add the tip to the food cost
    total_cost = food_cost + tip

    # return the result
    result = total_cost
    return result

print(solution())