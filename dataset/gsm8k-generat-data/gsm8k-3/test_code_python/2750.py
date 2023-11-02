def solution():
    """Zoe made a total of $8,000 cleaning pools and babysitting. She babysat Julie three times as often as she babysat Zachary. The number of times she babysat Zachary was 1/5 the number of times she babysat Chloe. If Zoe made $600 babysitting Zachary, how much did she earn from pool cleaning?"""
    # Define the amount Zoe made babysitting Zachary
    zachary_earnings = 600

    # Calculate the number of times Zoe babysat Zachary
    zachary_count = 1

    # Calculate the number of times Zoe babysat Chloe
    chloe_count = 5 * zachary_count

    # Calculate the number of times Zoe babysat Julie
    julie_count = 3 * zachary_count

    # Calculate the total amount Zoe made from babysitting
    babysitting_earnings = (zachary_earnings * zachary_count) + ((zachary_earnings * julie_count) / 3)

    # Calculate the amount Zoe made from pool cleaning
    pool_cleaning_earnings = 8000 - babysitting_earnings

    # Display the amount Zoe made from pool cleaning
    result = pool_cleaning_earnings
    return result

print(solution())