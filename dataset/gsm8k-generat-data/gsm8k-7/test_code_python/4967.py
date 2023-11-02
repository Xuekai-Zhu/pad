def solution():
    max_capacity = 350000
    loss_rate_1 = 32000
    loss_hours_1 = 5
    loss_rate_2 = 10000
    loss_hours_2 = 10
    fill_rate = 40000
    fill_hours = 3

    # Calculate the total amount of water lost in the first phase
    water_lost_1 = loss_rate_1 * loss_hours_1

    # Calculate the remaining amount of water after the first phase
    remaining_water_1 = max_capacity - water_lost_1

    # Calculate the total amount of water lost in the second phase
    water_lost_2 = loss_rate_2 * loss_hours_2

    # Calculate the remaining amount of water after the second phase
    remaining_water_2 = remaining_water_1 - water_lost_2

    # Calculate the total amount of water filled in the third phase
    water_filled = fill_rate * fill_hours

    # Calculate the final amount of water in the tank
    final_amount = remaining_water_2 + water_filled

    # Calculate the amount of water missing to reach the maximum capacity
    missing_amount = max_capacity - final_amount
    result = missing_amount
    return result

print(solution())