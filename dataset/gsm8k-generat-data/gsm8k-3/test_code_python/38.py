def solution():
    """Artemis is making tea for a party. She knows her mom drinks an 8-ounce cup of tea and uses one ounce of tea. She will use this same ratio for the party. The party has 12 people there and each of them wants a 6-ounce cup of tea. How many ounces of tea does she need?"""
    # Define the ratio of tea to water for one cup
    tea_ratio = 1 / 8

    # Calculate the total amount of tea needed based on the number of cups and their size
    cups = 12
    cup_size = 6
    total_ounces = cups * cup_size
    tea_needed = total_ounces * tea_ratio

    # Return the amount of tea needed in ounces
    result = tea_needed
    return result

print(solution())