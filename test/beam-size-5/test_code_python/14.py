def solution():
    eggs_per_omelet = 3  # Claire makes a 3 egg omelet every morning
    days_per_week = 7  # There are 7 days in a week
    weeks = 4  # Claire wants to know how many eggs she will eat in 4 weeks

    # Calculate the total number of eggs Claire will eat in 4 weeks
    total_eggs = eggs_per_omelet * days_per_week * weeks
    result = total_eggs
    return result

print(solution())