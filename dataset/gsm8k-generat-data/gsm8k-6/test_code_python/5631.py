def solution():
    # Calculate the total number of hours Kim had before dropping a class
    total_hours = 4 * 2  # Kim takes 4 classes that last 2 hours each

    # Calculate the total number of hours Kim has now after dropping one class
    new_total_hours = total_hours - 2  # Kim drops one 2-hour class

    # Convert the total number of hours to hours per day
    hours_per_day = new_total_hours / 4  # Kim now has 3 classes that last 2 hours each
    result = hours_per_day
    return result

print(solution())