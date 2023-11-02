def solution():
    # Calculate the total cost of the meal for both Billy and Jenny
    total_meal_cost = (20 + 5) * 2  # they each order a $20 steak and a $5 drink

    # Calculate the amount of the tip for the meal
    tip = 0.2 * total_meal_cost

    # Calculate the amount Billy needs to pay for 80% of the tip
    billy_tip = 0.8 * tip

    result = billy_tip
    return result

print(solution())