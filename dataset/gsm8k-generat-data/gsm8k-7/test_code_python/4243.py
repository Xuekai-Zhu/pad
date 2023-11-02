def solution():
    crown_cost = 20000
    tip_percentage = 0.1 # 10% tip

    # Calculate the amount of the tip
    tip_amount = crown_cost * tip_percentage

    # Calculate the total cost of the crown with the tip
    total_cost = crown_cost + tip_amount
    result = total_cost
    return result

print(solution())