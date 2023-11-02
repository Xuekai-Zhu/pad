def solution():
    """Lisa makes breakfast for her family every morning, Monday through Friday. She makes 2 eggs for each of her 4 children and 3 eggs for her husband. Then, she makes 2 eggs for herself. How many eggs does Lisa cook for her family for breakfast in a year?"""
    children_eggs = 2 * 4
    husband_eggs = 3
    lisa_eggs = 2
    total_eggs = children_eggs + husband_eggs + lisa_eggs
    days_per_week = 5
    weeks_per_year = 52
    eggs_per_year = total_eggs * days_per_week * weeks_per_year
    result = eggs_per_year
    return result

print(solution())