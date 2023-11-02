def solution():
    """Borgnine wants to see 1100 legs at the zoo. He has already seen 12 chimps, 8 lions, and 5 lizards. He is next headed to see the tarantulas. How many tarantulas does he need to see to meet his goal?"""
    total_legs_goal = 1100
    chimps_legs = 2 * 12
    lion_legs = 4 * 8
    lizard_legs = 4 * 5
    legs_seen_so_far = chimps_legs + lion_legs + lizard_legs
    tarantula_legs = 8
    tarantulas_needed = (total_legs_goal - legs_seen_so_far) / tarantula_legs
    result = tarantulas_needed
    return result

print(solution())