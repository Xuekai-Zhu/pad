def solution():
    cost_of_pizzas = 4 * 10  # Four pizzas at $10 each
    tip = 5  # Gemma gave a $5 tip to the delivery person
    total_cost = cost_of_pizzas + tip  # Total cost including tip
    paid_with = 50  # Gemma paid with a $50 bill

    # Calculate the change Gemma got back
    change = paid_with - total_cost
    result = change
    return result

print(solution())