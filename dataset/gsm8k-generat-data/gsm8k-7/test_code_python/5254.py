def solution():
    num_plain_pebbles = 40
    num_red_pebbles = 9
    num_blue_pebbles = 13

    # Calculate the number of pebbles that are not red or blue
    num_remainder_pebbles = num_plain_pebbles - num_red_pebbles - num_blue_pebbles

    # Calculate the number of pebbles in each of the three equal groups
    num_groups = 3
    num_remaining_groups = num_remainder_pebbles % num_groups
    num_purple_pebbles = (num_remainder_pebbles // num_groups) + num_remaining_groups
    num_yellow_pebbles = (num_remainder_pebbles // num_groups) + num_remaining_groups
    num_green_pebbles = num_remainder_pebbles // num_groups

    # Calculate the difference between the number of blue and yellow pebbles
    difference = num_blue_pebbles - num_yellow_pebbles
    result = difference
    return result

print(solution())