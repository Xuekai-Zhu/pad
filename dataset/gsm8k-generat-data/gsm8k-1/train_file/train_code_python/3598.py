def solution():
    """Victor, Austin, and Brian made traps to catch shrimp. Victor's trap caught 26 shrimp and Austin's trap caught 8 less than Victor's. Brian's trap caught half of Victor and Austin's total number of shrimp. If the boys then sold their shrimp for $7 for every 11 tails of shrimp and then divided their earnings equally amongst themselves, how much money does each boy make?"""
    victor_shrimp = 26
    austin_shrimp = victor_shrimp - 8
    total_shrimp = victor_shrimp + austin_shrimp
    brian_shrimp = total_shrimp / 2
    
    tails = total_shrimp * 2
    tails_divided = tails // 11
    
    earnings = tails_divided * 7
    earnings_per_person = earnings / 3
    
    result = earnings_per_person
    return result

print(solution())