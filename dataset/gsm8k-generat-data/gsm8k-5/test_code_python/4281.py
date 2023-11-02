def solution():
    pond_capacity = 200  # The pond can hold 200 gallons of water
    normal_pump_rate = 6  # The hose can normally pump 6 gallons per minute
    restricted_pump_rate = 2/3 * normal_pump_rate  # Due to drought restrictions, the pump can only operate at 2/3 of its normal rate

    # Calculate the total time it will take to fill the pond
    time_to_fill = pond_capacity / restricted_pump_rate

    result = time_to_fill
    return result

print(solution())