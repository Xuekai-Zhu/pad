def solution():
    """There are 6 forks in the cutlery drawer. There are 9 more knives than forks, and there are twice as many spoons as knives and half as many teaspoons as forks. After 2 of each cutlery is added to the drawer, how many pieces of cutlery are there in all?"""
    # Define the number of forks in the drawer
    forks = 6

    # Calculate the number of knives in the drawer
    knives = forks + 9

    # Calculate the number of spoons in the drawer
    spoons = knives * 2

    # Calculate the number of teaspoons in the drawer
    teaspoons = forks / 2

    # Add 2 of each type of cutlery to the drawer
    forks += 2
    knives += 2
    spoons += 2
    teaspoons += 2

    # Calculate the total number of cutlery pieces
    total_cutlery = forks + knives + spoons + teaspoons

    # Display the total number of cutlery pieces
    result = total_cutlery
    return result

print(solution())