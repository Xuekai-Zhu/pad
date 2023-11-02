def solution():
    # Calculate the total number of hours in a day
    total_hours = 24

    # Subtract the time Claire spends cleaning and cooking
    remaining_hours = total_hours - 4 - 2

    # Divide the remaining time equally between crafting and tailoring
    crafting_hours = remaining_hours / 2

    # Subtract the hours Claire spends sleeping
    crafting_hours -= 8

    result = crafting_hours
    return result

print(solution())