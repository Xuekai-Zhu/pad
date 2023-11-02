def solution():
    """At peak season, 6 packs of tuna fish are sold per hour, while in a low season 4 tuna packs are sold per hour. If each tuna pack is sold at $60, How much more money is made in a day during a high season than a low season if the fish are sold for 15 hours?"""
    # Define the price of each tuna pack and the number of hours the fish are sold
    TUNA_PACK_PRICE = 60
    HOURS_SOLD = 15

    # Calculate the total number of tuna packs sold in a high season
    high_season_packs = 6 * HOURS_SOLD

    # Calculate the total number of tuna packs sold in a low season
    low_season_packs = 4 * HOURS_SOLD

    # Calculate the total income in a high season
    high_season_income = high_season_packs * TUNA_PACK_PRICE

    # Calculate the total income in a low season
    low_season_income = low_season_packs * TUNA_PACK_PRICE

    # Calculate the difference in income between high and low seasons
    income_difference = high_season_income - low_season_income

    # Return the result
    result = income_difference
    return result

print(solution())