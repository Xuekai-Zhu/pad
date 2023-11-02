def solution():
    """A football team shares a single water cooler during practice.  During practice, linemen get the first water break and will drink 8 ounces each.  Skill position players get the second water break and drink 6 ounces each.  The team has 12 linemen and 10 skill position players.  If the cooler holds 126 ounces of water, how many skill position players must wait for the cooler to be refilled before they can get a drink?"""
    # Define the amount of water each player drinks
    LINEMAN_DRINK = 8
    SKILL_DRINK = 6

    # Define the number of linemen and skill position players
    num_linemen = 12
    num_skill = 10

    # Calculate the total amount of water the linemen drink
    lineman_water = num_linemen * LINEMAN_DRINK

    # Calculate the total amount of water the skill position players drink
    skill_water = num_skill * SKILL_DRINK

    # Calculate the total amount of water used during the practice
    total_water = lineman_water + skill_water

    # Calculate how many skill position players must wait for the cooler to be refilled
    remaining_water = 126 - total_water
    skill_wait = remaining_water // SKILL_DRINK
    if remaining_water % SKILL_DRINK != 0:
        skill_wait += 1

    # Display how many skill position players must wait
    result = skill_wait
    return result

print(solution())