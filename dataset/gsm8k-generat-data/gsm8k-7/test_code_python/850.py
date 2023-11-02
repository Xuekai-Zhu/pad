def solution():
    viviana_vanilla_chips = 20
    susana_chocolate_chips = 25

    # Calculate the number of Viviana's chocolate chips using the information given
    viviana_chocolate_chips = susana_chocolate_chips + 5

    # Calculate the number of Susana's vanilla chips using the fraction given
    susana_vanilla_chips = (3/4) * viviana_vanilla_chips

    # Calculate the total number of chips they have together
    total_chips = viviana_vanilla_chips + viviana_chocolate_chips + susana_vanilla_chips + susana_chocolate_chips
    result = total_chips
    return result

print(solution())