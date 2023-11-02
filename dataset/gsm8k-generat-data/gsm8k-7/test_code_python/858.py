def solution():
    max_added_sugar = 150
    soft_drink_calories = 2500
    added_sugar_percentage = 0.05
    candy_added_sugar = 25

    # Calculate the amount of added sugar in the soft drink
    soft_drink_added_sugar = soft_drink_calories * added_sugar_percentage

    # Calculate the remaining amount of added sugar that Mark can consume
    remaining_added_sugar = max_added_sugar - soft_drink_added_sugar

    # Calculate the amount of added sugar that Mark exceeded by
    exceeded_added_sugar = max_added_sugar * 2

    # Calculate the number of bars of candy that Mark took
    candy_bars = exceeded_added_sugar / candy_added_sugar
    result = candy_bars
    return result

print(solution())