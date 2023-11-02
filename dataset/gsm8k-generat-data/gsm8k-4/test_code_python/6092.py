def solution():
    """Part of Stella's job is to restock the toilet paper in each of the 6 bathrooms at the bed and breakfast. She stocks 1 roll a day, every day of the week. She buys the toilet paper in bulk, and each pack contains 1 dozen rolls. After 4 weeks, how many packs of toilet paper dozen Stella buy?"""
    # Define the number of rolls used per day
    rolls_per_day = 6 * 1

    # Calculate the total number of rolls used in 4 weeks
    total_rolls_used = rolls_per_day * 7 * 4

    # Calculate the number of packs of toilet paper needed, assuming each pack contains 12 rolls
    packs_needed = total_rolls_used // 12

    # Round up to the nearest whole pack
    if total_rolls_used % 12 != 0:
        packs_needed += 1

    # Display the result
    result = packs_needed
    return result

print(solution())