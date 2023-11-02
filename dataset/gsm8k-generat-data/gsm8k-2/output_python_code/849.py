def solution():
    """Viviana has five more chocolate chips than Susana, while Susana has 3/4 as many vanilla chips as Viviana. If Viviana has 20 Vanilla chips and Susana 25 chocolate chips, calculate the total number of chips they have together."""
    susana_choc_chips = 25
    viviana_van_chips = 20
    viviana_choc_chips = viviana_van_chips + 5
    susana_van_chips = 0.75 * viviana_van_chips
    total_chips = susana_choc_chips + viviana_van_chips + viviana_choc_chips + susana_van_chips
    result = total_chips
    return result

print(solution())