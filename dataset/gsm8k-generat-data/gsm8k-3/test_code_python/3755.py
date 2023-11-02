def solution():
    """A group of researchers are studying a colony of penguins. Their results show that the size doubled in the first year they watched the colony, then tripled in the next year. This year, however, harsh conditions meant the colony only gained 129 penguins. The colony has 1077 penguins in it now. Each penguin eats one and a half fish every day. How many fish did the whole colony catch per day to eat at the beginning of the first year?"""
    # Calculate the starting size of the colony
    starting_size = 1077 / 6

    # Calculate the size of the colony after the first year
    size_after_first_year = starting_size * 2

    # Calculate the size of the colony after the second year
    size_after_second_year = size_after_first_year * 3

    # Calculate the number of penguins added in the third year
    penguins_added_third_year = 129

    # Calculate the current size of the colony
    current_size = size_after_second_year + penguins_added_third_year

    # Calculate the number of fish the colony catches per day
    fish_per_day = current_size * 1.5

    # Display the number of fish caught per day
    result = fish_per_day
    return result

print(solution())