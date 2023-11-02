def solution():
    initial_sugar = 24  # The bag held 24 ounces of sugar before it was dropped
    sugar_removed_per_hour = 4  # The ants remove 4 ounces of sugar every hour
    hours_already_passed = 3  # The ants have already been harvesting sugar for 3 hours
    remaining_sugar = initial_sugar - (sugar_removed_per_hour * hours_already_passed)  # Calculate the amount of sugar remaining

    # Calculate the remaining time needed for the ants to harvest the remaining sugar
    remaining_time = remaining_sugar / sugar_removed_per_hour
    result = remaining_time
    return result

print(solution())