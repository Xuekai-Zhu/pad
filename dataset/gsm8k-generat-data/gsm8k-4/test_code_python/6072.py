def solution():
    """Sarah uses 1 ounce of shampoo, and one half as much conditioner as shampoo daily. In two weeks, what is the total volume of shampoo and conditioner, in ounces, that Sarah will use?"""
    # Define the amount of shampoo and conditioner used per day
    shampoo_daily = 1
    conditioner_daily = shampoo_daily / 2

    # Calculate the total amount of shampoo and conditioner used in two weeks (14 days)
    shampoo_total = shampoo_daily * 14
    conditioner_total = conditioner_daily * 14

    # Calculate the total volume of shampoo and conditioner
    total_volume = shampoo_total + conditioner_total

    # return the result
    result = total_volume
    return result

print(solution())