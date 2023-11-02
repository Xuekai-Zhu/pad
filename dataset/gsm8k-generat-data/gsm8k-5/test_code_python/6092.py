def solution():
    total_bathrooms = 6  # Stella has to restock the toilet paper in 6 bathrooms
    rolls_per_day = 1  # Stella stocks 1 roll per day
    days_per_week = 7  # There are 7 days in a week
    weeks = 4  # Stella wants to know how many packs of toilet paper dozen she will need after 4 weeks

    # Calculate the total number of rolls Stella will need in 4 weeks
    total_rolls = total_bathrooms * rolls_per_day * days_per_week * weeks

    # Calculate the number of packs of toilet paper dozen Stella will need, rounded up to the nearest integer
    packs_of_dozen = math.ceil(total_rolls / 12)
    result = packs_of_dozen
    return result

print(solution())