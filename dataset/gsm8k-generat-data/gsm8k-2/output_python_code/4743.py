def solution():
    """A football team shares a single water cooler during practice. During practice, linemen get the first water break and will drink 8 ounces each. Skill position players get the second water break and drink 6 ounces each. The team has 12 linemen and 10 skill position players. If the cooler holds 126 ounces of water, how many skill position players must wait for the cooler to be refilled before they can get a drink?"""
    lineman_ounces = 8 * 12
    skill_ounces = 6 * 10
    total_ounces_per_cycle = lineman_ounces + skill_ounces
    cycles_possible = 126 // total_ounces_per_cycle
    remaining_ounces = 126 - (cycles_possible * total_ounces_per_cycle)
    waiting_players = remaining_ounces // 6
    result = waiting_players
    return result

print(solution())