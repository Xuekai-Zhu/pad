def solution():
    starting_size = 0.5
    current_size = 1077
    growth_rate_1 = 2
    growth_rate_2 = 3
    gained_penguins = 129
    fish_per_penguin_per_day = 1.5

    # Calculate the starting size of the colony
    for i in range(2):
        starting_size *= growth_rate_1
    starting_size *= growth_rate_2

    # Calculate the total number of penguins at the end of the second year
    total_penguins = current_size - gained_penguins

    # Calculate the total number of fish needed per day
    total_fish_per_day = total_penguins * fish_per_penguin_per_day

    # Calculate the number of fish the colony caught per day at the beginning of the first year
    fish_caught_per_day = total_fish_per_day / starting_size
    result = fish_caught_per_day
    return result

print(solution())