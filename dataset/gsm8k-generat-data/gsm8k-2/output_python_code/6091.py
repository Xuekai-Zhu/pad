def solution():
    """Part of Stella's job is to restock the toilet paper in each of the 6 bathrooms at the bed and breakfast. She stocks 1 roll a day, every day of the week. She buys the toilet paper in bulk, and each pack contains 1 dozen rolls. After 4 weeks, how many packs of toilet paper dozen Stella buy?"""
    rolls_per_day = 6 * 1
    rolls_per_week = rolls_per_day * 7
    rolls_per_month = rolls_per_week * 4
    rolls_per_dozen = 12
    total_dozen = rolls_per_month / rolls_per_dozen
    result = total_dozen
    return result

print(solution())