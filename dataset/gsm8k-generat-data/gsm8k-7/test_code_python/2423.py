def solution():
    starting_volume = 100  # L
    rate = 2  # L/min
    time = 90  # min

    # Calculate the amount of water that flows into the tank during the heavy rain
    additional_volume = rate * time

    # Calculate the total volume of water in the tank at the end of the heavy rain
    final_volume = starting_volume + additional_volume
    result = final_volume
    return result

print(solution())