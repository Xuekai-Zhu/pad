def solution():
    babysitting_zachary = 600  # Zoe made $600 babysitting Zachary
    babysitting_julie = 3 * babysitting_zachary  # Zoe babysat Julie three times as often as Zachary
    babysitting_chloe = 5 * babysitting_zachary  # Zachary was babysat 1/5 as often as Chloe
    total_babysitting = babysitting_zachary + babysitting_julie + babysitting_chloe  # Total earned from babysitting
    pool_cleaning = 8000 - total_babysitting  # Total earned from pool cleaning
    result = pool_cleaning
    return result

print(solution())