def solution():
    """A group of researchers are studying a colony of penguins. Their results show that the size doubled in the first year they watched the colony, then tripled in the next year. This year, however, harsh conditions meant the colony only gained 129 penguins. The colony has 1077 penguins in it now. Each penguin eats one and a half fish every day. How many fish did the whole colony catch per day to eat at the beginning of the first year?"""
    # Calculate the number of penguins at the beginning of the second year
    penguins_second_year = 1077 - 129
    penguins_first_year = penguins_second_year / 3

    # Calculate the number of penguins at the beginning of the first year
    penguins_start = penguins_first_year / 2

    # Calculate the number of fish caught per day to feed the colony
    fish_per_day = penguins_start * 1.5

    return fish_per_day

print(solution())