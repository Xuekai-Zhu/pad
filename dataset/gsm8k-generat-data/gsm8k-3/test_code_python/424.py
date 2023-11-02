def solution():
    """Rose had 10 kilograms of rice. She cooked 9/10 kilograms in the morning and 1/4 of the remaining in the evening. How many grams of rice did she have left?"""
    # Convert 10kg to grams
    rice = 10000

    # Calculate the rice cooked in the morning
    rice_morning = int(rice * (9/10))

    # Calculate the rice remaining
    rice_remaining = rice - rice_morning

    # Calculate the rice cooked in the evening
    rice_evening = int(rice_remaining * (1/4))

    # Calculate the rice left
    rice_left = rice_remaining - rice_evening

    # Display the rice left in grams
    result = rice_left
    return result

print(solution())