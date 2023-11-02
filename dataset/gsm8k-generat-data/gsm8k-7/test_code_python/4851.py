def solution():
    num_silverware_per_type = 5
    num_extra_silverware_per_type = 10
    num_less_silverware_per_type = [4, 4, 5, 3]

    # Calculate the total number of silverware pieces for each type
    total_spoons = num_silverware_per_type + num_extra_silverware_per_type - num_less_silverware_per_type[0]
    total_butter_knives = num_silverware_per_type + num_extra_silverware_per_type - num_less_silverware_per_type[1]
    total_steak_knives = num_silverware_per_type + num_extra_silverware_per_type - num_less_silverware_per_type[2]
    total_forks = num_silverware_per_type + num_extra_silverware_per_type - num_less_silverware_per_type[3]

    # Calculate the total number of silverware pieces
    total_num_pieces = total_spoons + total_butter_knives + total_steak_knives + total_forks
    result = total_num_pieces
    return result

print(solution())