def solution():
    starting_temp = 20  # The dish starts at 20 degrees
    target_temp = 100  # The dish needs to reach 100 degrees to be ready
    heating_rate = 5  # The dish heats up by 5 degrees every minute

    # Calculate the time it will take to reach the target temperature
    minutes_to_heat = (target_temp - starting_temp) / heating_rate
    result = minutes_to_heat
    return result

print(solution())