def solution():
    # Define the number of potatoes
    num_potatoes = 2

    # Calculate the number of carrots (6 times the number of potatoes)
    num_carrots = 6 * num_potatoes

    # Calculate the number of onions (twice the number of carrots)
    num_onions = 2 * num_carrots

    # Calculate the number of green beans (1/3 the number of onions)
    num_green_beans = round(1/3 * num_onions)

    result = num_green_beans
    return result

print(solution())