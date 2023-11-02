def solution():
    num_total_chips = 10 / 0.1  # There are 100 chips in total if 10% are the blue chips
    num_blue_chips = 3
    num_white_chips = 0.5 * num_total_chips  # 50% of the chips are white
    num_green_chips = num_total_chips - num_blue_chips - num_white_chips  # The rest are green
    result = num_green_chips
    return result

print(solution())