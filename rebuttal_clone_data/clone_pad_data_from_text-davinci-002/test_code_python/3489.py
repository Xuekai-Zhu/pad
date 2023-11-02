def solution():
    total_contracts = 2
    contracts_per_shredding = 6
    total_units_to_shred = total_contracts * contracts_per_shredding
    total_shredding_sessions = total_units_to_shred / 6
    result = total_shredding_sessions
    return result

print(solution())