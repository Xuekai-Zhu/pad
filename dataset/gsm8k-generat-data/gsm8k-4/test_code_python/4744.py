def solution():
    """A football team shares a single water cooler during practice. During practice, linemen get the first water break and will drink 8 ounces each. Skill position players get the second water break and drink 6 ounces each. The team has 12 linemen and 10 skill position players. If the cooler holds 126 ounces of water, how many skill position players must wait for the cooler to be refilled before they can get a drink?"""
    # Define the number of linemen and skill position players
    num_linemen = 12
    num_skill_players = 10

    # Define the amount of water each linemen and skill position player drinks
    lineman_water = 8
    skill_water = 6

    # Calculate the total amount of water consumed by the linemen
    lineman_total_water = num_linemen * lineman_water

    # Calculate the amount of water remaining in the cooler
    remaining_water = 126 - lineman_total_water

    # Calculate the maximum number of skill position players that can drink from the remaining water
    max_skill_players = remaining_water // skill_water

    # Calculate the number of skill position players that must wait for the cooler to be refilled
    waiting_skill_players = num_skill_players - max_skill_players

    # return the result
    result = waiting_skill_players
    return result

print(solution())