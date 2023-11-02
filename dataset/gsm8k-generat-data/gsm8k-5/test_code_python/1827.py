def solution():
    # Calculate the number of eggs Lisa makes for her children each day
    eggs_for_children = 2 * 4  # Lisa makes 2 eggs for each of her 4 children

    # Calculate the total number of eggs Lisa makes for her family each day
    total_eggs = eggs_for_children + 3 + 2  # Lisa makes 3 eggs for her husband and 2 for herself

    # Calculate the total number of eggs Lisa makes for her family in a week
    weekly_eggs = total_eggs * 5  # Lisa makes breakfast Monday through Friday

    # Calculate the total number of eggs Lisa makes for her family in a year
    yearly_eggs = weekly_eggs * 52  # There are 52 weeks in a year

    result = yearly_eggs
    return result

print(solution())