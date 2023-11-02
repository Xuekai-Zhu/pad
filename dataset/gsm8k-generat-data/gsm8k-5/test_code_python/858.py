def solution():
    max_added_sugar = 150  # Maximum recommended added sugar intake for men per day
    soft_drink_added_sugar = 0.05 * 2500  # Soft drink contained 5% added sugar
    candy_added_sugar = 25  # Each bar of candy contained 25 calories of added sugar

    # Calculate the total added sugar Mark consumed
    total_added_sugar = soft_drink_added_sugar + (candy_added_sugar * x)

    # Calculate the maximum added sugar Mark could consume to stay within recommended limits
    max_consumable_added_sugar = max_added_sugar / 2

    # Calculate the number of bars of candy Mark consumed
    x = (total_added_sugar - max_consumable_added_sugar) / candy_added_sugar

    result = x
    return result

print(solution())