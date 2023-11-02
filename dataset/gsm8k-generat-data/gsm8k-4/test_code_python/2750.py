def solution():
    """Zoe made a total of $8,000 cleaning pools and babysitting. She babysat Julie three times as often as she babysat Zachary. The number of times she babysat Zachary was 1/5 the number of times she babysat Chloe. If Zoe made $600 babysitting Zachary, how much did she earn from pool cleaning?"""
    # Define the total amount Zoe made
    total_amount = 8000

    # Define the amount Zoe made from babysitting
    babysitting_amount = 600 + 3 * 600  # babysitting Zachary + babysitting Julie

    # Calculate the amount Zoe made from pool cleaning
    pool_cleaning_amount = total_amount - babysitting_amount

    # return the result
    result = pool_cleaning_amount
    return result

print(solution())