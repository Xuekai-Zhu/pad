def solution():
    pond_capacity = 200
    normal_pump_rate = 6 # gallons/minute
    current_pump_rate = 2/3 * normal_pump_rate

    # Calculate the number of minutes it will take to fill the pond
    time_to_fill = pond_capacity / current_pump_rate
    result = time_to_fill
    return result

print(solution())