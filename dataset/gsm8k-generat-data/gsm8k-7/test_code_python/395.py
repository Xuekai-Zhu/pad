def solution():
    initial_num_elephants = 30000
    exiting_rate = 2880
    exiting_time = 4
    entering_time = 7
    final_num_elephants = 28980

    # Calculate the number of elephants that exited the park during the exodus
    num_exiting = exiting_rate * exiting_time

    # Calculate the number of elephants remaining in the park after the exodus
    num_remaining = initial_num_elephants - num_exiting

    # Calculate the rate at which new elephants entered the park
    entering_rate = (final_num_elephants - num_remaining) / entering_time
    result = entering_rate
    return result

print(solution())