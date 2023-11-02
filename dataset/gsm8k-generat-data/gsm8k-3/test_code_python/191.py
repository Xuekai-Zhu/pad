def solution():
    """In a section of the forest, there are 100 weasels and 50 rabbits. Three foxes invade this region and hunt the rodents. Each fox catches an average of 4 weasels and 2 rabbits per week. How many rabbits and weasels will be left after 3 weeks?"""
    # Define the initial number of weasels and rabbits
    initial_weasels = 100
    initial_rabbits = 50

    # Define the number of weeks the foxes hunt
    weeks = 3

    # Define the number of foxes
    foxes = 3

    # Calculate the number of weasels and rabbits caught by the foxes each week
    weasels_caught_per_week = foxes * 4
    rabbits_caught_per_week = foxes * 2

    # Calculate the total number of weasels and rabbits caught over the entire hunting period
    total_weasels_caught = weasels_caught_per_week * weeks
    total_rabbits_caught = rabbits_caught_per_week * weeks

    # Calculate the remaining number of weasels and rabbits
    remaining_weasels = initial_weasels - total_weasels_caught
    remaining_rabbits = initial_rabbits - total_rabbits_caught

    # Return the result as a tuple
    result = (remaining_weasels, remaining_rabbits)
    return result

print(solution())