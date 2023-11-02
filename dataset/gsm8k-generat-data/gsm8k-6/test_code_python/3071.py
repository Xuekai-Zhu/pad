def solution():
    # Find the total number of hours Claire has for crafting and tailoring
    total_hours = 24 - 8 - 4 - 2  # total number of hours in a day minus 8 hours of sleep, 4 hours of cleaning, and 2 hours of cooking
    hours_per_activity = total_hours / 2  # divide the remaining hours equally between crafting and tailoring

    # Find the number of hours Claire spent crafting
    crafting_hours = hours_per_activity
    result = crafting_hours
    return result

print(solution())