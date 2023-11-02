def solution():
    starting_num_stamps = 40
    percent_increase = 0.20

    # Calculate the number of additional stamps Maria wants to collect
    additional_stamps = starting_num_stamps * percent_increase

    # Calculate the total number of stamps Maria wants to collect
    total_num_stamps = starting_num_stamps + additional_stamps
    result = total_num_stamps
    return result

print(solution())