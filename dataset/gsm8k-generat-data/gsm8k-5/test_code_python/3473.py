def solution():
    eggs_ordered = 3 * 12  # Tricia ordered three dozen eggs
    eggs_for_crepes = eggs_ordered * (1/4)  # Tricia will use 1/4 of the eggs for crepes
    eggs_remaining = eggs_ordered - eggs_for_crepes  # Eggs remaining after making crepes
    eggs_for_cupcakes = eggs_remaining * (2/3)  # Tricia will use 2/3 of the remaining eggs for cupcakes
    eggs_left_for_breakfast = eggs_remaining - eggs_for_cupcakes  # Eggs left for breakfast

    result = eggs_left_for_breakfast
    return result

print(solution())