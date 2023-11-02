def solution():
    # Calculate how many meters they ran with 6 laps
    meters_per_lap = 150
    meters_run = 2 * meters_per_lap * 6

    # Calculate how many laps they still have to run to reach 2400 meters
    total_meters = 2400
    meters_left = total_meters - meters_run
    laps_left = meters_left / (2 * meters_per_lap)
    result = laps_left
    return result

print(solution())