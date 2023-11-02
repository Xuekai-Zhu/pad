def solution():
    num_black_beans = 8
    num_green_beans = num_black_beans + 2
    num_orange_beans = num_green_beans - 1

    # Calculate the total number of jellybeans in the bag
    total_beans = num_black_beans + num_green_beans + num_orange_beans
    result = total_beans
    return result

print(solution())