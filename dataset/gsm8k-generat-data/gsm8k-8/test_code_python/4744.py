def solution():
    # Calculate the total amount of water consumed by the linemen
    linemen_water = 8 * 12

    # Calculate the remaining amount of water in the cooler after the linemen drink
    remaining_water = 126 - linemen_water

    # Calculate the maximum number of skill position players who can drink from the remaining water
    max_skill_players = remaining_water // 6

    # Calculate the number of skill position players who must wait for the cooler to be refilled
    waiting_skill_players = 10 - max_skill_players

    result = waiting_skill_players
    return result

print(solution())