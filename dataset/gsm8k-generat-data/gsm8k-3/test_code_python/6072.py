def solution():
    """Sarah uses 1 ounce of shampoo, and one half as much conditioner as shampoo daily.  In two weeks, what is the total volume of shampoo and conditioner, in ounces, that Sarah will use?"""
    
    # Calculate the amount of conditioner used daily
    conditioner_daily = 0.5

    # Calculate the total amount of shampoo and conditioner used in two weeks
    shampoo_total = 14 * 1
    conditioner_total = 14 * conditioner_daily

    # Calculate the total volume of shampoo and conditioner used
    total_volume = shampoo_total + conditioner_total

    # Display the total volume
    result = total_volume
    return result

print(solution())