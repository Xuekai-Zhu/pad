def solution():
    # Define the number of mangoes Alexis has
    alexis_mangoes = 60

    # Calculate the combined number of mangoes Dilan and Ashley have
    combined_mangoes = alexis_mangoes / 4

    # Calculate Dilan's number of mangoes
    dilan_mangoes = combined_mangoes / 2

    # Calculate Ashley's number of mangoes
    ashley_mangoes = combined_mangoes / 2

    # Calculate the total number of mangoes
    total_mangoes = alexis_mangoes + dilan_mangoes + ashley_mangoes
    result = total_mangoes
    return result

print(solution())