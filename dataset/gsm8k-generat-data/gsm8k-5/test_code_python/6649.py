def solution():
    # Calculate the total distance Charlie ran
    total_distance = 3 * 2.5  # Charlie ran around the field 2 1/2 times, so he covered 3 km x 2.5 = 7.5 km

    # Calculate the number of steps Charlie took per kilometer
    steps_per_km = 5350 / 3  # Charlie took 5350 steps while running on a 3-km field

    # Calculate the total number of steps Charlie took during the running session
    total_steps = steps_per_km * total_distance
    result = total_steps
    return result

print(solution())