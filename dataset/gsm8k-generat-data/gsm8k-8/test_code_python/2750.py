def solution():
    # Calculate the number of times Zoe babysat Zachary
    zachary_babysitting = 1/5 * chloe_babysitting
    # Calculate the number of times Zoe babysat Julie
    julie_babysitting = 3 * zachary_babysitting
    # Calculate the total amount earned from babysitting
    babysitting_earnings = 600 + (julie_babysitting + zachary_babysitting) * babysitting_rate
    # Calculate the amount earned from pool cleaning
    pool_cleaning_earnings = total_earnings - babysitting_earnings
    result = pool_cleaning_earnings
    return result

print(solution())