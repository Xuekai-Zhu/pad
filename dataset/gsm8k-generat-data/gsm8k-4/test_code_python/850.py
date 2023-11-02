def solution():
    """Viviana has five more chocolate chips than Susana, while Susana has 3/4 as many vanilla chips as Viviana. If Viviana has 20 Vanilla chips and Susana 25 chocolate chips, calculate the total number of chips they have together."""
    
    # Given Viviana has 20 Vanilla chips, Susana has 3/4 as many vanilla chips as Viviana
    susana_vanilla_chips = (3/4)*20

    # Given Susana has 25 chocolate chips and Viviana has five more chocolate chips than Susana
    viviana_choco_chips = 25 + 5
    susana_choco_chips = 25

    # Total number of chips together
    total_chips = viviana_choco_chips + susana_choco_chips + susana_vanilla_chips + 20

    # Calculate and return the result
    result = total_chips
    return result

print(solution())