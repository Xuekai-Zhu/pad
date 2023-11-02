def solution():
    # Calculate the total number of bread loaves baked in 6 hours
    breads_per_hour = 10
    total_breads = breads_per_hour * 6

    # Calculate the total number of baguettes baked in 6 hours
    baguettes_per_2_hours = 30
    total_baguettes = baguettes_per_2_hours * 3

    # Add the total number of bread loaves and baguettes
    total_baked = total_breads + total_baguettes
    result = total_baked
    return result

print(solution())