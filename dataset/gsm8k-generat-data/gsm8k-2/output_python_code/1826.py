def solution():
    """Lisa makes breakfast for her family every morning, Monday through Friday. She makes 2 eggs for each of her 4 children and 3 eggs for her husband. Then, she makes 2 eggs for herself. How many eggs does Lisa cook for her family for breakfast in a year?"""
    eggs_per_person = {"children": 2, "husband": 3, "Lisa": 2}
    total_family_members = len(eggs_per_person)
    days_per_week = 5
    weeks_per_year = 52
    total_eggs = 0
    for day in range(days_per_week):
        for person, eggs in eggs_per_person.items():
            total_eggs += eggs
    total_eggs *= total_family_members
    total_eggs *= weeks_per_year
    result = total_eggs
    return result

print(solution())