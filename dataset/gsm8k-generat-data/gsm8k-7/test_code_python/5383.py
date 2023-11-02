def solution():
    start_wood = 10
    end_wood = 3
    morning_burn = 4

    # Calculate the total amount of wood burned in the morning
    total_morning_burn = morning_burn

    # Calculate the total amount of wood burned throughout the day
    total_burn = start_wood - end_wood
    afternoon_burn = total_burn - morning_burn

    # Calculate the amount of wood burned in the afternoon
    num_afternoon_burn = afternoon_burn
    result = num_afternoon_burn
    return result

print(solution())