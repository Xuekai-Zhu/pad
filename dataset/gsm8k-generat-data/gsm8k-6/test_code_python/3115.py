def solution():
    # Calculate the number of red beans
    red_beans = 572 / 4

    # Calculate the number of remaining beans
    remaining_beans = 572 - red_beans

    # Calculate the number of white beans
    white_beans = remaining_beans / 3

    # Calculate the number of remaining beans
    remaining_beans = remaining_beans - white_beans

    # Calculate the number of green beans
    green_beans = remaining_beans / 2

    result = green_beans
    return result

print(solution())