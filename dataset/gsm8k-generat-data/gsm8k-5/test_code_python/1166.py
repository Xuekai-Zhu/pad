def solution():
    crickets_per_three_days = 70  # A gecko eats 70 crickets every three days
    first_day_percentage = 0.3  # On the first day, the gecko eats 30% of the crickets
    first_day_crickets = crickets_per_three_days * first_day_percentage  # Calculate the number of crickets eaten on the first day
    second_day_crickets = first_day_crickets - 6  # On the second day, the gecko eats 6 less crickets than the first
    remaining_crickets = crickets_per_three_days - first_day_crickets - second_day_crickets  # Calculate the number of remaining crickets
    third_day_crickets = remaining_crickets  # On the third day, the gecko finishes up the remaining crickets

    result = third_day_crickets
    return result

print(solution())