def solution():
    # Calculate the total cost of the meal
    meal_cost = 40 + 15 + 25

    # Calculate the service charge
    service_charge = meal_cost * 0.1

    # Calculate the total cost of the meal plus service charge
    total_cost = meal_cost + service_charge

    # Calculate the tip
    tip = total_cost * 0.05

    # Calculate the final bill amount
    final_bill = total_cost + tip

    # Calculate the change from $100
    change = 100 - final_bill
    result = change
    return result

print(solution())