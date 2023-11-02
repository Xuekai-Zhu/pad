def solution():
    # Calculate the total amount of water filled in the first hour
    first_hour = 8  # gallons of water filled in the first hour

    # Calculate the total amount of water filled in the next two hours
    next_two_hours = 2 * 10  # gallons of water filled in the next two hours

    # Calculate the total amount of water filled in the fourth hour
    fourth_hour = 14  # gallons of water filled in the fourth hour

    # Calculate the total amount of water filled in the first four hours
    first_four_hours = first_hour + next_two_hours + fourth_hour

    # Calculate the total amount of water in the pool after four hours
    total_after_four_hours = first_four_hours

    # Calculate the total amount of water in the pool after the leak in the fifth hour
    total_after_fifth_hour = total_after_four_hours - 8  # 8 gallons of water lost due to leak

    result = total_after_fifth_hour
    return result

print(solution())