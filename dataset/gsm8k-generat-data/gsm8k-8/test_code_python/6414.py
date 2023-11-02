def solution():
    # Define the number of flies needed per animal per day
    flies_per_frog = 30
    frogs_per_fish = 8
    fish_per_gharial = 15

    # Calculate the total number of flies eaten by one gharial per day
    flies_per_gharial = fish_per_gharial * frogs_per_fish * flies_per_frog

    # Calculate the total number of flies eaten per day by all gharials
    total_flies_eaten = flies_per_gharial * 9
    result = total_flies_eaten
    return result

print(solution())