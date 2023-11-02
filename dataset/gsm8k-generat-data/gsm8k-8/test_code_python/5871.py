def solution():
    # Define the cost of the haircuts
    tayzia_haircut_cost = 48
    daughters_haircut_cost = 2 * 36

    # Calculate the total cost of the haircuts
    total_haircut_cost = tayzia_haircut_cost + daughters_haircut_cost

    # Calculate the tip amount
    tip_percentage = 20
    tip_amount = total_haircut_cost * (tip_percentage / 100)

    result = tip_amount
    return result

print(solution())