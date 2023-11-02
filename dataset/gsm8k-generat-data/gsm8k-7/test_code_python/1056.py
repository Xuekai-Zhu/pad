def solution():
    num_potatoes = 2

    # Calculate the number of carrots needed, which is six times the number of potatoes
    num_carrots = 6 * num_potatoes

    # Calculate the number of onions needed, which is twice the number of carrots
    num_onions = 2 * num_carrots

    # Calculate the number of green beans needed, which is 1/3 the number of onions
    num_green_beans = num_onions / 3

    result = num_green_beans
    return result

print(solution())