def solution():
    # Calculate the total distance Charlie ran
    total_distance = 3 * 2.5  # Charlie ran around the field 2 1/2 times
    # Calculate the number of steps Charlie can take per kilometer
    steps_per_kilometer = 5350 / 3
    # Calculate the total number of steps Charlie took during the running session
    total_steps = steps_per_kilometer * total_distance
    result = total_steps
    return result

print(solution())