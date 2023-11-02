def solution():
    cherries_per_quart = 500
    cherries_picked_per_hour = 300/2  # 150 cherries per hour
    hours_to_make_syrup_per_quart = 3
    num_quarts = 9

    # Calculate the total number of cherries needed
    total_cherries_needed = cherries_per_quart * num_quarts

    # Calculate the total number of hours to pick enough cherries
    total_hours_to_pick_cherries = total_cherries_needed / cherries_picked_per_hour

    # Calculate the total hours to make the syrup
    total_hours_to_make_syrup = hours_to_make_syrup_per_quart * num_quarts

    # Calculate the total time required
    total_time_required = total_hours_to_pick_cherries + total_hours_to_make_syrup
    result = total_time_required
    return result

print(solution())