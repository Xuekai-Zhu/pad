def solution():
    num_hatch_per_day = 3000
    num_lost_per_day = 900
    day_count = 7
    initial_num_bees = 12500

    # Calculate the net change in bees per day
    net_change_per_day = num_hatch_per_day - num_lost_per_day

    # Calculate the total net change in bees over the course of the 7 days
    total_net_change = net_change_per_day * day_count

    # Calculate the total number of bees in the hive at the end of 7 days
    total_num_bees = initial_num_bees + total_net_change
    result = total_num_bees
    return result

print(solution())