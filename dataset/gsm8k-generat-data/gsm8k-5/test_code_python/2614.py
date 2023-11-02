def solution():
    starting_eggs = 2 * 12  # Megan bought 1 dozen eggs and her neighbor gave her another dozen
    eggs_used_for_dinner = 2 + 4  # Megan used 2 eggs for an omelet and 4 eggs for a cake
    remaining_eggs = starting_eggs - eggs_used_for_dinner  # Megan has this many eggs remaining
    eggs_given_to_aunt = remaining_eggs / 2  # Megan gave her aunt half of her remaining eggs
    eggs_for_next_3_meals = remaining_eggs - eggs_given_to_aunt  # Megan has this many eggs left for her next 3 meals
    eggs_per_meal = eggs_for_next_3_meals / 3  # Megan will divide her remaining eggs equally for 3 meals
    result = eggs_per_meal
    return result

print(solution())