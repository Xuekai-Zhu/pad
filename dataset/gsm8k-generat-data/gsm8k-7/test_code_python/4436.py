def solution():
    cost_of_phone = 1300
    percent_already_saved = 0.4

    # Calculate the amount of money Mike already has
    amount_already_saved = cost_of_phone * percent_already_saved

    # Calculate the remaining amount of money Mike needs to save
    amount_to_save = cost_of_phone - amount_already_saved
    result = amount_to_save
    return result

print(solution())