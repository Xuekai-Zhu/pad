def solution():
    # Calculate the starting size of the colony
    starting_size = 1077 / 6

    # Calculate the size of the colony at the end of the first year
    first_year_size = starting_size / 2

    # Calculate the size of the colony at the end of the second year
    second_year_size = first_year_size * 3

    # Calculate the total change in size of the colony over the first two years
    total_size_change = second_year_size - starting_size

    # Calculate the average number of fish eaten per day by each penguin
    fish_per_penguin = 1.5

    # Calculate the total number of fish eaten per day by the whole colony at the beginning of the first year
    fish_per_day = total_size_change * fish_per_penguin

    result = fish_per_day
    return result

print(solution())