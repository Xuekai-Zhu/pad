def solution():
    black_beans = 8  # The bag contains 8 black jellybeans
    green_beans = black_beans + 2  # The bag contains 2 more green jellybeans than black jellybeans
    orange_beans = green_beans - 1  # The bag contains 1 less orange jellybean than green jellybeans

    # Calculate the total number of jellybeans in the bag
    total_beans = black_beans + green_beans + orange_beans
    result = total_beans
    return result

print(solution())