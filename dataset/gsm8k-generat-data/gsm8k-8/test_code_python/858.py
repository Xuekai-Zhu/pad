def solution():
    # Calculate the amount of added sugar in the soft drink
    soft_drink_added_sugar = 0.05 * 2500

    # Calculate the remaining amount of added sugar needed to reach the recommended intake
    remaining_added_sugar = 1.5 * 150 - soft_drink_added_sugar

    # Calculate the number of candy bars needed to reach the remaining added sugar
    candy_bars_needed = remaining_added_sugar / 25

    # Calculate the number of candy bars actually taken
    candy_bars_taken = 2 * candy_bars_needed

    result = candy_bars_taken
    return result

print(solution())