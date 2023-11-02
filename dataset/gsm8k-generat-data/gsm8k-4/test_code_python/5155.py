def solution():
    """There are 6 forks in the cutlery drawer. There are 9 more knives than forks, and there are twice as many spoons as knives and half as many teaspoons as forks. After 2 of each cutlery is added to the drawer, how many pieces of cutlery are there in all?"""
    # Define the initial number of forks
    forks = 6

    # Calculate the number of knives
    knives = forks + 9

    # Calculate the number of spoons
    spoons = knives * 2

    # Calculate the number of teaspoons
    teaspoons = forks / 2

    # Calculate the total number of cutlery before adding 2 of each
    total_cutlery = forks + knives + spoons + teaspoons

    # Calculate the total number of cutlery after adding 2 of each
    total_cutlery += 2 * 4

    # return the result
    result = total_cutlery
    return result

print(solution())