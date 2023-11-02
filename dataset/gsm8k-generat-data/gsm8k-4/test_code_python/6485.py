def solution():
    """My age is five times that of my son. Next year, my son will be eight years old. How old am I now?"""
    # Define the age of the son next year
    son_next_year_age = 8

    # Calculate the current age of the son
    son_current_age = son_next_year_age - 1

    # Calculate the current age of the parent
    parent_current_age = son_current_age * 5

    result = parent_current_age
    return result

print(solution())