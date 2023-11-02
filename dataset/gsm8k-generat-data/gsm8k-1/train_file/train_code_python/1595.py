def solution():
    """Nina loves to travel. She tries to travel at least 400 kilometers in one month outside of her home country.
    Every second month she does twice that distance. If she were able to keep up with her resolution, how many kilometers would
    she travel during 2 years?"""
    
    distance_per_month = 400
    distance_every_other_month = 2 * distance_per_month
    months_per_year = 12
    total_distance = 0
    
    # calculate distance for each month for 2 years
    for i in range(24):
        if i % 2 == 0:  # every other month
            total_distance += distance_every_other_month
        else:
            total_distance += distance_per_month
    
    # calculate total distance for 2 years
    total_distance *= months_per_year
    
    result = total_distance
    return result

print(solution())