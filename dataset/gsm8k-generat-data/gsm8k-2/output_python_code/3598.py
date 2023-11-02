def solution():
    """Victor, Austin, and Brian made traps to catch shrimp. Victor's trap caught 26 shrimp and Austin's trap caught 8 less than Victor's. Brian's trap caught half of Victor and Austin's total number of shrimp. If the boys then sold their shrimp for $7 for every 11 tails of shrimp and then divided their earnings equally amongst themselves, how much money does each boy make?"""
    victors_catch = 26
    austins_catch = victors_catch - 8
    total_catch = victors_catch + austins_catch
    brians_catch = total_catch / 2
    total_tails = (victors_catch + austins_catch + brians_catch) * 2
    earnings = (total_tails // 11) * 7
    earnings_per_person = earnings / 3
    result = earnings_per_person
    return result

print(solution())