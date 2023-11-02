def solution():
    # Calculate the size of the colony in the first year
    size_first_year = 1077 // 6  # the size doubled in the first year, so the initial size was 1/2 of the current size
    # Calculate the size of the colony in the second year
    size_second_year = size_first_year * 3  # the size tripled in the second year
    # Calculate the total number of penguins in the colony
    total_penguins = size_first_year + size_second_year + 129  # the colony gained 129 penguins this year
    # Calculate the total number of fish the colony eats per day
    total_fish = total_penguins * 1.5  # each penguin eats 1.5 fish per day
    result = total_fish
    return result

print(solution())