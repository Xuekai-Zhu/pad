def solution():
    # Shenny will wear the same shirt on Monday and Sunday
    shirts_on_monday_and_sunday = 1

    # Shenny will wear two different shirts each other day, for a total of 5 days
    shirts_on_other_days = 2 * 5

    # Total number of shirts needed
    total_shirts = shirts_on_monday_and_sunday + shirts_on_other_days
    result = total_shirts
    return result

print(solution())