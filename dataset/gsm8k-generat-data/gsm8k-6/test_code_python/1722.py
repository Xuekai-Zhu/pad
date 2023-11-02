def solution():
    # Calculate the time taken for each part of the race
    time_part_1 = 3 / 150  # time taken for first 3 km at 150 km/hr
    time_part_2 = 2 / (150 + 50)  # time taken for next 2 km at 50 km/hr faster than first 3 km
    time_part_3 = 1 / (2 * 150)  # time taken for last 1 km at twice the speed of first 3 km

    # Calculate the total time taken and distance travelled
    total_time = time_part_1 + time_part_2 + time_part_3
    total_distance = 6

    # Calculate the average speed for the entire race
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())