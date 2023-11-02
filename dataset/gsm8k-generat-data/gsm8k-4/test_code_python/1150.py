def solution():
    """A driver travels 30 miles per hour for 3 hours and 25 miles per hour for 4 hours to deliver goods to a town every day from Monday to Saturday. How many miles does the driver travel in a week? """
    # Define the distances and times for each day
    monday_distance = 30 * 3 + 25 * 4
    tuesday_distance = 30 * 3 + 25 * 4
    wednesday_distance = 30 * 3 + 25 * 4
    thursday_distance = 30 * 3 + 25 * 4
    friday_distance = 30 * 3 + 25 * 4
    saturday_distance = 30 * 3 + 25 * 4

    # Calculate the total distance traveled in the week
    total_distance = monday_distance + tuesday_distance + wednesday_distance + thursday_distance + friday_distance + saturday_distance

    # Return the result
    result = total_distance
    return result

print(solution())