def solution():
    """The centerpieces at Glenda’s wedding reception include a fishbowl containing 2 fish, except for one table that has 3 fish. There are 32 tables. How many fish are there?"""
    # Define the number of tables with 2 fish and 3 fish
    tables_2_fish = 31
    tables_3_fish = 1

    # Calculate the total number of fish
    total_fish = tables_2_fish * 2 + tables_3_fish * 3

    # Display the total number of fish
    result = total_fish
    return result

print(solution())