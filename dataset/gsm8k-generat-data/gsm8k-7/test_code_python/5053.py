def solution():
    minutes_per_hour = 60
    minutes_per_color_change = 10
    num_hours = 2

    # Calculate the number of color changes that occur in one hour
    changes_per_hour = minutes_per_hour / minutes_per_color_change

    # Calculate the total number of color changes that occur over the two hour sunset
    total_changes = changes_per_hour * num_hours
    result = total_changes
    return result

print(solution())