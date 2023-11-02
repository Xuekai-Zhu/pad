def solution():
    initial_goldfish = 18
    death_rate = 5
    new_goldfish_per_week = 3
    num_weeks = 7

    # Calculate the total number of goldfish that die after num_weeks
    total_deaths = num_weeks * death_rate

    # Calculate the total number of new goldfish that Martin purchases after num_weeks
    total_new_goldfish = num_weeks * new_goldfish_per_week

    # Calculate the total number of goldfish that Martin will have after num_weeks
    total_goldfish = initial_goldfish - total_deaths + total_new_goldfish
    result = total_goldfish
    return result

print(solution())