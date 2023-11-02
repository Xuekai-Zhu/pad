def solution():
    # Calculate the total distance run by Jackson in the first week
    first_week_distance = 3 

    # Calculate the total distance run by Jackson in the next 4 weeks
    additional_distance = 1 + 2 + 3 + 4 

    # Calculate the total distance run by Jackson after 5 weeks
    total_distance = first_week_distance + additional_distance 

    # Calculate the average distance run by Jackson each day after 5 weeks
    average_distance = total_distance / 35 

    result = average_distance
    return result

print(solution())