def solution():
    # Calculate the length of time John was on his first mission
    original_time = 5
    extra_time = original_time * 0.6
    total_first_mission = original_time + extra_time

    # Calculate the length of time John was on his second mission
    second_mission = 3

    # Calculate the total length of time John was on missions
    total_missions = total_first_mission + second_mission
    result = total_missions
    return result

print(solution())