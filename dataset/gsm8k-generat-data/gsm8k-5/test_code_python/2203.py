def solution():
    eggs_in_fridge = 20  # Ben has 20 eggs in the fridge
    eggs_eaten_yesterday = 4 + 3  # Ben ate 4 eggs in the morning and 3 in the afternoon

    # Calculate the number of eggs Ben has now
    eggs_now = eggs_in_fridge - eggs_eaten_yesterday
    result = eggs_now
    return result

print(solution())