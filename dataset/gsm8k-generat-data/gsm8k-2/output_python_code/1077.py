def solution():
    """The centerpieces at Glenda’s wedding reception include a fishbowl containing 2 fish, except for one table that has 3 fish. There are 32 tables. How many fish are there?"""
    num_tables_with_2_fish = 31
    num_tables_with_3_fish = 1
    total_fish = (num_tables_with_2_fish * 2) + (num_tables_with_3_fish * 3)
    result = total_fish
    return result

print(solution())