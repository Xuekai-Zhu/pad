def solution():
    num_tables_with_2_fish = 31
    num_fish_per_table_with_2_fish = 2
    num_fish_per_table_with_3_fish = 3

    # Calculate the total number of fish in tables with 2 fish
    total_fish_in_tables_with_2_fish = num_tables_with_2_fish * num_fish_per_table_with_2_fish

    # Calculate the number of fish in the table with 3 fish
    num_fish_in_table_with_3_fish = num_fish_per_table_with_3_fish

    # Calculate the total number of fish
    total_fish = total_fish_in_tables_with_2_fish + num_fish_in_table_with_3_fish
    result = total_fish
    return result

print(solution())