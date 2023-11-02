def solution():
    num_ladies = 4
    group_walk_miles = 3
    jamie_additional_miles = 2
    sue_additional_miles = 1
    num_days = 6

    # Calculate the total miles walked by the group on their daily walk
    group_total_miles = num_ladies * group_walk_miles

    # Calculate the total additional miles that Jamie walks
    jamie_total_miles = jamie_additional_miles * num_days

    # Calculate the total additional miles that Sue walks
    sue_total_miles = (jamie_additional_miles / 2) * num_days

    # Calculate the total miles walked by all the ladies
    total_miles = (group_total_miles + jamie_total_miles + sue_total_miles) * num_days
    result = total_miles
    return result

print(solution())