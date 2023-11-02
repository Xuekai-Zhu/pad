def solution():
    # Calculate the number of bees that leave the hive in the first 6 hours
    leave_first_6_hours = 30

    # Calculate the number of bees that leave the hive fly from the hive in the next 6 hours
    fly_first_6_hours = leave_first_6_hours * 2

    # Calculate the number of bees that leave the hive fly from the hive in the next 6 hours
    fly_next_6_hours = fly_first_6_hours * 2

    # Calculate the number of bees that leave the hive in the last 6 hours
    last_6_hours = leave_first_6_hours + fly_next_6_hours

    result = last_6_hours
    return result

print(solution())