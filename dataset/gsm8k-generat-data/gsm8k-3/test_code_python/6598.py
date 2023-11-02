def solution():
    """Ariel is collecting fish. She has 45 fish. 2/3 are male. How many female fish does she have?"""
    # Define the total number of fish and the fraction that are male
    total_fish = 45
    male_fraction = 2/3

    # Calculate the number of male fish
    male_fish = total_fish * male_fraction

    # Calculate the number of female fish
    female_fish = total_fish - male_fish

    # Display the number of female fish
    result = female_fish
    return result

print(solution())