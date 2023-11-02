def solution():
    # Define the number of black beans and green beans
    black_beans = 8
    green_beans = black_beans + 2

    # Calculate the number of orange beans
    orange_beans = green_beans - 1

    # Calculate the total number of jellybeans
    total_beans = black_beans + green_beans + orange_beans
    result = total_beans
    return result

print(solution())