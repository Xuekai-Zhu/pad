def solution():
    # Calculate the total number of days from November 1 to February 28
    total_days = 31 + 31 + 30 + 28  # November has 30 days, December has 31, January has 31, February has 28

    # Calculate the total number of firewood logs needed for 5 logs a day
    total_logs = 5 * total_days

    # Calculate the total number of trees needed
    trees_needed = total_logs / 75  # each tree gives 75 pieces of firewood

    result = trees_needed
    return result

print(solution())