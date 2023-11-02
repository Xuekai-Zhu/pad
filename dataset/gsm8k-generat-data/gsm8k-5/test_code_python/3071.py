def solution():
    total_working_hours = 24 - 8  # Claire has 24 hours in a day, but she sleeps for 8 hours
    time_cleaning = 4  # Claire has 4 hours to clean
    time_cooking = 2  # Claire has 2 hours to cook

    # Calculate the total amount of time Claire has for crafting and tailoring
    remaining_time = total_working_hours - time_cleaning - time_cooking
    time_each = remaining_time / 2  # Divide the remaining time equally between crafting and tailoring

    # Calculate the time Claire spent crafting
    crafting_time = time_each
    result = crafting_time
    return result

print(solution())