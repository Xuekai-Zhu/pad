def solution():
    num_children = 2
    diaper_changes_per_child_per_day = 5
    wife_changes_per_day = diaper_changes_per_child_per_day / 2

    # Calculate the total number of diapers Jordan has
    total_diapers = num_children * diaper_changes_per_child_per_day

    # Calculate the number of diapers Jordan's wife changes per day
    num_wife_changes_per_day = total_diapers / 2

    # Calculate the total number of diapers Jordan changes per day
    total_changes_per_day = num_wife_changes_per_day + num_wife_changes_per_day
    result = total_changes_per_day
    return result

print(solution())