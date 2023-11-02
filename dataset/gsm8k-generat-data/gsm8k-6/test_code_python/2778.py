def solution():
    # Calculate the number of laps Lexi needs to run to complete 3 and 1/4 miles
    total_miles = 3.25
    lap_distance = 0.25
    num_laps = total_miles / lap_distance
    result = int(num_laps)  # round down to nearest integer
    return result

print(solution())