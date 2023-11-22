def solution():
    
    # Define the number of bees that leave in the first 6 hours
    first_6_hours_bees = 30

    # Calculate the number of bees that return in the next 6 hours
    next_6_hours_bees = first_6_hours_bees / 2

    # Calculate the number of bees that leave in the next 6 hours
    next_6_hours_bees_leave = first_6_hours_bees * 2

    # Calculate the number of bees that left in the next 6 hours
    remaining_bees = first_6_hours_bees - next_6_hours_bees_leave

    # Calculate the number of bees that return to the hive in the last 6 hours
    last_6_hours_bees_returned = remaining_bees * 6

    # Display the number of bees that return to the hive in the last 6 hours
    result = last_6_hours_bees_returned
    return result

print(solution())