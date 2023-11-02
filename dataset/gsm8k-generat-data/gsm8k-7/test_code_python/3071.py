def solution():
    total_working_hours = 24
    cleaning_hours = 4
    cooking_hours = 2
    sleeping_hours = 8

    # Calculate the total hours spent on cleaning, cooking, and sleeping
    total_non_working_hours = cleaning_hours + cooking_hours + sleeping_hours

    # Calculate the total hours available for crafting and tailoring
    total_crafting_tailoring_hours = total_working_hours - total_non_working_hours

    # Calculate the number of hours per activity
    hours_per_activity = total_crafting_tailoring_hours / 2

    # Calculate the number of hours spent crafting
    crafting_hours = hours_per_activity
    result = crafting_hours
    return result

print(solution())