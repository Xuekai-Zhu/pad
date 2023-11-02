def solution():
    # Calculate the total amount of water consumed by linemen
    linemen_water = 8 * 12  # linemen get 8 ounces each and there are 12 linemen

    # Calculate the total amount of water consumed by skill position players
    skill_players_water = 6 * 10  # skill players get 6 ounces each and there are 10 skill players

    # Calculate the total amount of water consumed by the team
    total_water = linemen_water + skill_players_water

    # Calculate the number of skill position players who must wait for the cooler to be refilled
    wait_players = (total_water - 126) // 6  # 126 ounces is the maximum capacity of the cooler, and each skill player drinks 6 ounces

    result = wait_players
    return result

print(solution())