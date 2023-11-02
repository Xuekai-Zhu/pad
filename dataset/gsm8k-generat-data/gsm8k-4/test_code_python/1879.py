def solution():
    """On their way driving to Los Angeles, Benjamin and James see lots of billboard ads. Curious, Benjamin starts to count how many they see. In the first hour once he starts counting he counts 17 billboards. In the second hour once he starts counting he sees 20 billboards. In the third hour he sees 23 billboards. James asks Benjamin the average number of billboards they've seen per hour. What should Benjamin tell him?"""
    # Define the total number of billboards and the number of hours
    total_billboards = 17 + 20 + 23
    num_hours = 3

    # Calculate the average number of billboards per hour
    avg_billboards_per_hour = total_billboards / num_hours

    # Round the average to the nearest integer
    avg_billboards_per_hour = round(avg_billboards_per_hour)

    # return the result
    result = avg_billboards_per_hour
    return result

print(solution())