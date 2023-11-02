def solution():
    """A group of researchers are studying a colony of penguins. Their results show that the size doubled in the first year they watched the colony, then tripled in the next year. This year, however, harsh conditions meant the colony only gained 129 penguins. The colony has 1077 penguins in it now. Each penguin eats one and a half fish every day. How many fish did the whole colony catch per day to eat at the beginning of the first year?"""
    initial_size = 1077 / 6  # assuming the growth was consistent across the three years
    first_year_size = initial_size / 2
    second_year_size = first_year_size * 3
    final_size = second_year_size + 129
    total_fish_per_day = final_size * 1.5
    result = total_fish_per_day
    return result

print(solution())