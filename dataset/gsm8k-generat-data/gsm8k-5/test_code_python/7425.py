def solution():
    # Calculate the number of loaves of bread Lars can make in 6 hours
    loaves_per_hour = 10
    hours_baking_bread = 6
    total_loaves = loaves_per_hour * hours_baking_bread

    # Calculate the number of baguettes Lars can make in 6 hours
    baguettes_per_two_hours = 30
    total_baguettes = baguettes_per_two_hours * 3  # Lars bakes for 6 hours, which is 3 sets of 2 hours

    # Calculate the total number of breads Lars makes in 6 hours
    total_breads = total_loaves + total_baguettes
    
    result = total_breads
    return result

print(solution())