def solution():
    total_distance = 3.25
    lap_distance = 0.25

    # Divide the total distance by the distance of one lap
    total_laps = total_distance / lap_distance

    # Round up to the nearest whole number of laps
    complete_laps = math.ceil(total_laps)

    result = complete_laps
    return result

print(solution())