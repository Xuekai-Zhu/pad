def solution():
    viviana_vanilla_chips = 20
    susana_chocolate_chips = 25
    susana_vanilla_chips = (3/4)*viviana_vanilla_chips
    viviana_chocolate_chips = susana_chocolate_chips + 5
    
    # Calculate total number of chips
    total_chips = viviana_vanilla_chips + susana_vanilla_chips + viviana_chocolate_chips + susana_chocolate_chips
    result = total_chips
    return result

print(solution())