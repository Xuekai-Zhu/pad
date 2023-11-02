def solution():
    # Define the number of lions as 200
    lions = 200

    # Calculate the number of leopards as half the number of lions
    leopards = lions / 2

    # Calculate the total number of lions and leopards
    total_lions_leopards = lions + leopards

    # Calculate the number of elephants as half the total number of lions and leopards
    elephants = total_lions_leopards / 2

    # Calculate the total population of the three animals
    total_population = lions + leopards + elephants

    result = total_population
    return result

print(solution())