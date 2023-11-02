def solution():
    height_of_hoop = 10  # in feet
    minimum_reach_to_dunk = 6 / 12  # in feet
    player_height = 6  # in feet
    wingspan_reach = 22 / 12  # in feet

    # Calculate the total reach of the player
    total_reach = player_height + wingspan_reach

    # Calculate how much the player needs to jump in order to reach minimum reach to dunk
    jump_height = minimum_reach_to_dunk - (height_of_hoop - total_reach)

    result = jump_height
    return result

print(solution())