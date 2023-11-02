def solution():
    # Define the total number of crickets she eats in three days
    total_crickets = 70

    # Calculate the number of crickets she eats on the first day
    first_day_crickets = 0.3 * total_crickets

    # Calculate the number of crickets she eats on the second day
    second_day_crickets = first_day_crickets - 6

    # Calculate the number of crickets she eats on the third day
    third_day_crickets = total_crickets - first_day_crickets - second_day_crickets
    result = third_day_crickets
    return result

print(solution())