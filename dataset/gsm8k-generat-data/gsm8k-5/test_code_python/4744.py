def solution():
    lineman_ounces = 8  # each lineman drinks 8 ounces
    skill_ounces = 6  # each skill position player drinks 6 ounces
    total_linemen = 12  # there are 12 linemen
    total_skill = 10  # there are 10 skill position players
    total_ounces = 126  # the cooler holds 126 ounces

    # Calculate how many total ounces the linemen will drink
    lineman_total_ounces = lineman_ounces * total_linemen

    # Calculate how many total ounces the skill position players will drink
    skill_total_ounces = skill_ounces * total_skill

    # Calculate the remaining ounces in the cooler after linemen drink
    remaining_ounces = total_ounces - lineman_total_ounces

    # Calculate how many skill position players can still get a drink
    skill_players_left = remaining_ounces // skill_ounces

    # Calculate how many skill position players must wait for the cooler to be refilled
    waiting_players = total_skill - skill_players_left

    result = waiting_players
    return result

print(solution())