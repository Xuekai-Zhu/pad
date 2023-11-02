def solution():
    """Terese thinks that running various distances throughout the week can make one healthy.  On Monday, she runs 4.2 miles;  Tuesday, 3.8 miles; Wednesday, 3.6 miles; and on Thursday, 4.4 miles.  Determine the average distance Terese runs on each of the days she runs."""
    # Define the distances Terese runs on each day
    monday_distance = 4.2
    tuesday_distance = 3.8
    wednesday_distance = 3.6
    thursday_distance = 4.4

    # Calculate the total distance Terese runs in a week
    total_distance = monday_distance + tuesday_distance + wednesday_distance + thursday_distance

    # Calculate the average distance Terese runs on each day
    average_distance = total_distance / 4

    # return the result
    result = average_distance
    return result

print(solution())