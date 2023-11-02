def solution():
    bag_size = 100
    total_beans = 3 * bag_size
    ratio_of_colors = {'red': 24,
                       'white': 18}
    total_red_beans = ratio_of_colors['red']
    total_white_beans = ratio_of_colors['white']
    total_reds_and_whites = total_red_beans + total_white_beans
    result = total_reds_and_whites
    return result

print(solution())