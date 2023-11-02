def solution():
    """A group of researchers are studying a colony of penguins. Their results show that the size doubled in the first year they watched the colony, then tripled in the next year. This year, however, harsh conditions meant the colony only gained 129 penguins. The colony has 1077 penguins in it now. Each penguin eats one and a half fish every day. How many fish did the whole colony catch per day to eat at the beginning of the first year?"""
    starting_size = 1077 / 6  # find the original size by working backwards from the current size
    year1_size = starting_size * 2
    year2_size = year1_size * 3
    penguins_caught_fish = starting_size + year1_size + year2_size + 129
    fish_per_penguin_per_day = 1.5
    total_fish_per_day = penguins_caught_fish * fish_per_penguin_per_day
    result = total_fish_per_day
    return result

print(solution())