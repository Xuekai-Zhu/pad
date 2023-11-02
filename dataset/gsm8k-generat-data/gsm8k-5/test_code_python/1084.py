def solution():
    meal_cost = 20 + 5  # The cost of one meal is $20 for the steak and $5 for the drink
    total_cost = meal_cost * 2  # There are two people, so the total cost is double the meal cost
    tip_percentage = 0.2  # The tip is 20% of the total cost
    desired_tip_coverage = 0.8  # Billy wants to cover 80% of the tip for both of them

    # Calculate the total amount of the tip
    total_tip = total_cost * tip_percentage

    # Calculate the amount Billy needs to pay to cover 80% of the tip
    billy_tip = total_tip * desired_tip_coverage / 2  # Divide by 2 because there are two people

    result = billy_tip
    return result

print(solution())