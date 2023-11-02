def solution():
    # Calculate the time it took Coby to travel from Washington to Idaho
    time_to_idaho = 640 / 80  # distance divided by speed

    # Calculate the time it took Coby to travel from Idaho to Nevada
    time_to_nevada = 550 / 50  # distance divided by speed

    # Calculate the total time of the trip
    total_time = time_to_idaho + time_to_nevada

    result = total_time
    return result

print(solution())