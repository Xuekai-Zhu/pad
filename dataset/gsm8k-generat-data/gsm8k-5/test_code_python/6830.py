def solution():
    red_hat_count = 6
    blue_boot_count = 9
    both_count = 3

    # Total number of gingerbread men
    total_count = red_hat_count + blue_boot_count - both_count

    # Percentage of gingerbread men with red hats
    red_hat_percent = (red_hat_count - both_count) / total_count * 100
    result = red_hat_percent
    return result

print(solution())