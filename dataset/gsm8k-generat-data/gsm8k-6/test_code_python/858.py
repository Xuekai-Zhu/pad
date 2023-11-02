def solution():
    # Calculate the number of calories from added sugar in the soft drink
    added_sugar_softdrink = 0.05 * 2500  # 5% of the soft drink's calories are from added sugar

    # Calculate the maximum added sugar Mark can consume for the day
    max_added_sugar = 150  # the recommended intake of added sugar per day

    # Calculate the actual amount of added sugar Mark consumed
    actual_added_sugar = 2 * max_added_sugar  # Mark exceeded the recommended intake by 100%

    # Calculate the number of bars of candy Mark consumed
    candy_calories = actual_added_sugar - added_sugar_softdrink  # the remaining calories from added sugar he can consume
    candy_bars = candy_calories / 25  # each bar of candy contains 25 calories of added sugar

    result = candy_bars
    return result

print(solution())