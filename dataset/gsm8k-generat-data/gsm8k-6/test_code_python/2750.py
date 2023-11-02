def solution():
    # Calculate the number of times Zoe babysat Zachary and Chloe
    babysitting_zachary = 1
    babysitting_chloe = 5 * babysitting_zachary

    # Calculate the number of times Zoe babysat Julie
    babysitting_julie = 3 * babysitting_zachary
    
    # Calculate the total amount earned from babysitting
    total_babysitting = (babysitting_zachary * 600) + (babysitting_chloe + babysitting_julie) * 50
    
    # Calculate the amount earned from pool cleaning 
    pool_cleaning = 8000 - total_babysitting
    
    result = pool_cleaning
    return result

print(solution())