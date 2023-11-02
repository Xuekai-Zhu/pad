def solution():
    """Lisa makes breakfast for her family every morning, Monday through Friday. She makes 2 eggs for each of her 4 children and 3 eggs for her husband. Then, she makes 2 eggs for herself. How many eggs does Lisa cook for her family for breakfast in a year?"""
    # Define the number of family members
    family_members = 6

    # Define the number of eggs per person
    eggs_per_person = [2, 2, 2, 2, 3, 2]

    # Calculate the total number of eggs cooked each day
    eggs_per_day = sum(eggs_per_person)

    # Calculate the total number of eggs cooked in a year
    eggs_per_year = eggs_per_day * 5 * 52

    # return the result
    result = eggs_per_year
    return result

print(solution())