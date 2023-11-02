def solution():
    """Viviana has five more chocolate chips than Susana, while Susana has 3/4 as many vanilla chips as Viviana. If Viviana has 20 Vanilla chips and Susana 25 chocolate chips, calculate the total number of chips they have together."""
    susana_choco = 25
    viviana_choco = susana_choco + 5
    viviana_vanilla = 20
    susana_vanilla = (3/4) * viviana_vanilla
    total_chips = susana_choco + viviana_choco + viviana_vanilla + susana_vanilla
    result = total_chips
    return result

print(solution())