def solution():
    """The centerpieces at Glenda's wedding reception include a fishbowl containing 2 fish, except for one table that has 3 fish. There are 32 tables. How many fish are there?"""
    normal_tables = 31  # Out of 32 total tables, 31 have 2 fish.
    fish_per_normal_table = 2
    fish_per_special_table = 3
    total_fish = normal_tables * fish_per_normal_table + fish_per_special_table
    result = total_fish
    return result

print(solution())