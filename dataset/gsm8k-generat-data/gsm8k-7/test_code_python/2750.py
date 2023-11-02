def solution():
    total_income = 8000
    income_from_Zachary = 600
    ratio_Zachary_Chloe = 1 / 5
    ratio_Julie_Zachary = 3

    # Calculate the total number of times Zoe babysat Zachary
    num_babysitting_Zachary = income_from_Zachary / (total_income / 2)

    # Calculate the number of times Zoe babysat Chloe
    num_babysitting_Chloe = num_babysitting_Zachary / ratio_Zachary_Chloe

    # Calculate the number of times Zoe babysat Julie
    num_babysitting_Julie = num_babysitting_Zachary * ratio_Julie_Zachary

    # Calculate the total income from babysitting
    income_from_babysitting = (num_babysitting_Zachary + num_babysitting_Chloe + num_babysitting_Julie) * income_from_Zachary

    # Calculate the income from pool cleaning
    income_from_pool_cleaning = total_income - income_from_babysitting

    result = income_from_pool_cleaning
    return result

print(solution())