def solution():
    # Define initial variables
    day = 1
    candy_bars_sold = 10
    total_earned = 0

    # Calculate earnings for each day and add to total
    while day <= 6:
        earnings = candy_bars_sold * 0.10
        total_earned += earnings

        # Increase number of candy bars sold for next day
        candy_bars_sold += 4

        # Increase day counter
        day += 1

    # Convert earnings to dollars and round to two decimal places
    total_earned = round(total_earned, 2)
    result = total_earned
    return result

print(solution())