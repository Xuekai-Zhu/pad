def solution():
    """Part of Stella's job is to restock the toilet paper in each of the 6 bathrooms at the bed and breakfast.  She stocks 1 roll a day, every day of the week.  She buys the toilet paper in bulk, and each pack contains 1 dozen rolls.  After 4 weeks, how many packs of toilet paper dozen Stella buy?"""
    # Define the number of rolls needed per day
    ROLLS_PER_DAY = 6 * 1

    # Calculate the total number of rolls needed for 4 weeks
    total_rolls_needed = ROLLS_PER_DAY * 7 * 4

    # Calculate the number of packs of toilet paper dozen needed
    packs_needed = total_rolls_needed // 12

    # Display the number of packs needed
    result = packs_needed
    return result

print(solution())