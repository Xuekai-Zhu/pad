def solution():
    tables_with_two_fish = 31
    tables_with_three_fish = 1
    fish_per_table = 2
    total_fish = (tables_with_two_fish * fish_per_table) + (tables_with_three_fish * fish_per_table)
    result = total_fish
    return result

print(solution())