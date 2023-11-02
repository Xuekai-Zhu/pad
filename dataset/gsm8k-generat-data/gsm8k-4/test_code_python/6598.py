def solution():
    """Ariel is collecting fish. She has 45 fish. 2/3 are male. How many female fish does she have?"""
    # Define the total number of fish and the proportion of male fish
    total_fish = 45
    male_proportion = 2/3

    # Calculate the number of male fish and the number of female fish
    male_fish = total_fish * male_proportion
    female_fish = total_fish - male_fish

    # Return the number of female fish
    result = female_fish
    return result

print(solution())