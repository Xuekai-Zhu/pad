def solution():
    anna_sweeping_time = 10 * 3  # 30 minutes
    billy_laundry_time = 2 * 9  # 18 minutes

    # Calculate the total amount of time Anna and Billy have spent on chores so far
    total_time = anna_sweeping_time + billy_laundry_time

    # Divide the total time evenly between Anna and Billy
    time_per_person = total_time / 2

    # Calculate how many dishes Billy should wash to spend the same amount of time as Anna
    billy_dishes_time = time_per_person - billy_laundry_time  # Subtract Billy's laundry time from total time
    num_dishes = billy_dishes_time / 2  # 2 minutes per dish
    result = num_dishes
    return result

print(solution())