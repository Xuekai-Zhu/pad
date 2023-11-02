def solution():
    # Calculate the percentage of mornings Jake drops his coffee
    dropped_coffee_percentage = 0.4 * 0.25  # 40% of mornings he trips, and 25% of the time he trips he drops his coffee
    not_dropped_coffee_percentage = 100 - dropped_coffee_percentage  # Calculate the percentage of mornings he does not drop his coffee
    result = not_dropped_coffee_percentage
    return result

print(solution())