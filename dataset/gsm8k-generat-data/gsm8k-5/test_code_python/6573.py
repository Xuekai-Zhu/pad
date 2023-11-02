def solution():
    initial_temp = 60  # Starting temperature of candy mixture
    final_temp = 170  # Final temperature needed
    heating_rate = 5  # Candy heats at 5 degrees/minute
    cooling_rate = 7  # Candy cools at 7 degrees/minute

    # Calculate time needed to heat up the mixture
    time_to_heat = (240 - 60) / heating_rate

    # Calculate time needed to cool down the mixture
    time_to_cool = (240 - 170) / cooling_rate

    # Total time needed
    total_time = time_to_heat + time_to_cool
    result = total_time
    return result

print(solution())