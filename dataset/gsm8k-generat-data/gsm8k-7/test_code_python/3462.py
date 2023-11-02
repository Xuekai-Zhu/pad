def solution():
    initial_cats = 1800
    first_mission_cats = 600
    remaining_cats_after_first_mission = initial_cats - first_mission_cats

    # Calculate the number of cats remaining after the second mission
    remaining_cats_after_second_mission = remaining_cats_after_first_mission / 2

    result = remaining_cats_after_second_mission
    return result

print(solution())