def solution():
    # Number of cats originally on the island
    original_cats = 1800

    # Number of cats relocated on the first mission
    first_mission_cats = 600

    # Number of cats remaining after the first mission
    remaining_cats = original_cats - first_mission_cats

    # Number of cats relocated on the second mission
    second_mission_cats = remaining_cats / 2

    # Number of cats remaining after the second mission
    final_cats = remaining_cats - second_mission_cats

    result = final_cats
    return result

print(solution())