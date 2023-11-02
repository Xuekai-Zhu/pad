def solution():
    """Lars owns a bakeshop. She can bake 10 loaves of bread within an hour and 30 baguettes every 2 hours. If she bakes 6 hours a day, how many breads does she makes?"""
    # Calculate the total number of loaves of bread Lars can make in 6 hours
    loaves_per_hour = 10
    total_loaves = loaves_per_hour * 6

    # Calculate the total number of baguettes Lars can make in 6 hours
    baguettes_per_two_hours = 30
    total_baguettes = baguettes_per_two_hours * 3

    # Calculate the total number of breads Lars makes in 6 hours
    total_breads = total_loaves + total_baguettes

    # Return the result
    result = total_breads
    return result

print(solution())