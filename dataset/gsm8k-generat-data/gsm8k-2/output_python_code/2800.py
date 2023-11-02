def solution():
    """Borgnine wants to see 1100 legs at the zoo. He has already seen 12 chimps, 8 lions, and 5 lizards. He is next headed to see the tarantulas. How many tarantulas does he need to see to meet his goal?"""
    total_legs = 1100
    chimps_legs = 2 * 12
    lions_legs = 4 * 8
    lizards_legs = 4 * 5
    seen_legs = chimps_legs + lions_legs + lizards_legs
    remaining_legs = total_legs - seen_legs
    tarantulas_legs = 8
    tarantulas_needed = remaining_legs // tarantulas_legs
    result = tarantulas_needed
    return result

print(solution())