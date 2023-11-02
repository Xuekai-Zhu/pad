def solution():
    """Susie has 572 beans in the jar. One-fourth of them are red and one-third of the remaining beans are white. Then half of the remaining are green beans. How many green beans are there?"""
    # Calculate the number of red beans
    red_beans = 572 / 4

    # Calculate the number of non-red beans
    non_red_beans = 572 - red_beans

    # Calculate the number of white beans
    white_beans = non_red_beans / 3

    # Calculate the number of non-white beans
    non_white_beans = non_red_beans - white_beans

    # Calculate the number of green beans
    green_beans = non_white_beans / 2

    # Display the number of green beans
    result = green_beans
    return result

print(solution())