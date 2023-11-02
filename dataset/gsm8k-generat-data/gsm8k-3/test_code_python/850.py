def solution():
    """Viviana has five more chocolate chips than Susana, while Susana has 3/4 as many vanilla chips as Viviana. If Viviana has 20 Vanilla chips and Susana 25 chocolate chips, calculate the total number of chips they have together."""
    # Define the number of vanilla chips Viviana has
    viviana_vanilla_chips = 20

    # Calculate the number of vanilla chips Susana has
    susana_vanilla_chips = viviana_vanilla_chips / (3/4)

    # Define the number of chocolate chips Susana has
    susana_chocolate_chips = 25

    # Calculate the number of chocolate chips Viviana has
    viviana_chocolate_chips = susana_chocolate_chips + 5

    # Calculate the total number of chips they have together
    total_chips = viviana_vanilla_chips + susana_vanilla_chips + susana_chocolate_chips + viviana_chocolate_chips

    # Display the total number of chips
    result = total_chips
    return result

print(solution())