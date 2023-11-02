def solution():
    num_blue_horses = 3
    num_purple_horses = 3 * num_blue_horses
    num_green_horses = 2 * num_purple_horses
    num_gold_horses = num_green_horses / 6

    # Calculate the total number of horses
    total_horses = num_blue_horses + num_purple_horses + num_green_horses + num_gold_horses
    result = total_horses
    return result

print(solution())