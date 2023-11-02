def solution():
    # Define Brian's starting time (in seconds)
    starting_time = 10

    # Double his time after the first week
    week1_time = starting_time * 2

    # Double his time again after the second week
    week2_time = week1_time * 2

    # Increase his time by 50% after the third week
    week3_time = week2_time * 1.5

    # Calculate his final time
    final_time = week3_time

    result = final_time
    return result

print(solution())