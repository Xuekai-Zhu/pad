def solution():
    """Lisa makes breakfast for her family every morning, Monday through Friday. She makes 2 eggs for each of her 4 children and 3 eggs for her husband. Then, she makes 2 eggs for herself. How many eggs does Lisa cook for her family for breakfast in a year?"""
    # Define the number of weekdays in a year
    WEEKDAYS_YEAR = 260

    # Calculate the number of eggs Lisa makes each day
    children_eggs = 2 * 4
    husband_eggs = 3
    lisa_eggs = 2
    total_eggs = children_eggs + husband_eggs + lisa_eggs

    # Calculate the total number of eggs Lisa makes in a year
    yearly_eggs = total_eggs * WEEKDAYS_YEAR

    # Display the total number of eggs Lisa makes in a year
    result = yearly_eggs
    return result

print(solution())