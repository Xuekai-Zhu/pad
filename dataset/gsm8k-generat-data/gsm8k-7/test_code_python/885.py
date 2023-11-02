def solution():
    mold_cost = 250
    labor_cost_per_hour = 75
    hours_worked = 8
    discount_on_labor = 0.8

    # Calculate the total cost of labor
    total_labor_cost = labor_cost_per_hour * hours_worked

    # Apply the discount on labor
    discounted_labor_cost = total_labor_cost * discount_on_labor

    # Calculate the total cost of the shoes
    total_cost = mold_cost + discounted_labor_cost
    result = total_cost
    return result

print(solution())