def solution():
    total_miles = 3.25
    lap_length = 0.25

    # Calculate the total number of laps she needs to run
    num_laps = total_miles / lap_length

    # Round up to the nearest integer since she can't run a partial lap
    num_laps = math.ceil(num_laps)

    result = num_laps
    return result

print(solution())