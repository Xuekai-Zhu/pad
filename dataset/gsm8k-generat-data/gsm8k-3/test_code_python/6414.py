def solution():
    """Each frog needs to eat 30 flies per day to live. Each fish needs to eat 8 frogs per day to live. Each gharial needs to eat 15 fish a day to live. How many flies get eaten every day in this swamp if it has 9 gharials?"""
    # Define the number of gharials in the swamp
    num_gharials = 9

    # Calculate the number of fish needed to feed the gharials
    num_fish = num_gharials * 15

    # Calculate the number of frogs needed to feed the fish
    num_frogs = num_fish * 8

    # Calculate the number of flies needed to feed the frogs
    num_flies = num_frogs * 30

    # Display the number of flies eaten per day
    result = num_flies
    return result

print(solution())