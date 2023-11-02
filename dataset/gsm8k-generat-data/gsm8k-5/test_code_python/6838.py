def solution():
    original_time = 5  # John's first mission was supposed to take 5 days
    extra_time_percent = 60  # But it took 60% longer than expected
    extra_time = original_time * (extra_time_percent/100)  # Calculate the extra time in days
    total_time = original_time + extra_time  # Add the extra time to the original time

    second_mission_time = 3  # John's second mission took 3 days

    # Calculate the total time John was on missions
    total_mission_time = total_time + second_mission_time
    result = total_mission_time
    return result

print(solution())