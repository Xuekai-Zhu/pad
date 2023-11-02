def solution():
    num_starting_socks = 40
    num_lost_socks = 4
    num_donated_socks = (2/3) * (num_starting_socks - num_lost_socks)
    num_new_purchased_socks = 10
    num_new_gifted_socks = 3

    # Calculate the total number of socks Caroline has after all events
    total_socks = num_starting_socks - num_lost_socks + num_new_purchased_socks + num_new_gifted_socks - num_donated_socks
    result = total_socks
    return result

print(solution())