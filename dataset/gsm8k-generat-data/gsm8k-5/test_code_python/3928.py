def solution():
    time_to_paint_house = 20 / 60  # Convert 20 minutes to hours, to get the time to paint one house
    hours_available = 3  # We have 3 hours available
    houses_painted = hours_available // time_to_paint_house  # Calculate how many houses we can paint
    
    result = houses_painted
    return result

print(solution())