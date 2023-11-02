def solution():
    max_capacity = 350000  # The tank has a maximum capacity of 350,000 gallons

    # Calculate the total amount of water lost during the first 5 hours
    water_loss_first_5_hours = 32000 * 5  # The tank is losing 32,000 gallons/hour for 5 hours

    # Calculate the total amount of water lost during the next 10 hours
    water_loss_next_10_hours = 10000 * 10  # The tank is losing 10,000 gallons/hour for 10 hours

    # Calculate the total amount of water that was not lost during the repair time
    remaining_water = max_capacity - water_loss_first_5_hours - water_loss_next_10_hours

    # Calculate the total amount of water that was added during the second attempt to fill the tank
    water_added_second_attempt = 40000 * 3  # The tank is being filled with 40,000 gallons/hour for 3 hours

    # Calculate the current amount of water in the tank
    current_amount_of_water = remaining_water + water_added_second_attempt

    # Calculate the amount of water missing to reach the maximum capacity
    missing_water = max_capacity - current_amount_of_water
    result = missing_water
    return result

print(solution())