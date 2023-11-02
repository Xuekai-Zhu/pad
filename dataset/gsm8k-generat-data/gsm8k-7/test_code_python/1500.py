def solution():
    smoky_salmon = 40
    black_burger = 15
    chicken_katsu = 25
    service_charge = 0.1
    tip = 0.05
    total_food_cost = smoky_salmon + black_burger + chicken_katsu

    # Calculate the amount of service charge
    service_charge_amount = total_food_cost * service_charge

    # Add the service charge to the total food cost
    total_with_service_charge = total_food_cost + service_charge_amount

    # Calculate the amount of tip
    tip_amount = total_with_service_charge * tip

    # Add the tip to the total with service charge
    total_paid = total_with_service_charge + tip_amount

    # Calculate the change
    change = 100 - total_paid
    result = change
    return result

print(solution())