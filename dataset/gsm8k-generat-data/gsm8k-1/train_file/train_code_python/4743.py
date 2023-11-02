def solution():
    """A football team shares a single water cooler during practice.
    During practice, linemen get the first water break and will drink 8 ounces each.
    Skill position players get the second water break and drink 6 ounces each.
    The team has 12 linemen and 10 skill position players.
    If the cooler holds 126 ounces of water, how many skill position players must wait for the cooler to be refilled before they can get a drink?"""
    lineman_drink = 8
    skill_drink = 6
    num_linemen = 12
    num_skill = 10
    total_water = 126

    # Calculate how much water linemen use
    linemen_water = num_linemen * lineman_drink

    # Calculate how much water skill position players use
    skill_water = num_skill * skill_drink

    # Calculate how much water is left after linemen drink
    remaining_water = total_water - linemen_water

    # Calculate how many skill position players can drink before the cooler needs to be refilled
    num_skill_drinks = int(remaining_water / skill_drink)

    # Calculate how many skill position players must wait for the cooler to be refilled
    num_waiting_skill = num_skill - num_skill_drinks

    result = num_waiting_skill
    return result

print(solution())