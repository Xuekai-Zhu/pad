def solution():
    """Grayson drives a motorboat for 1 hour at 25 mph and then 0.5 hours for 20 mph. Rudy rows in his rowboat for 3 hours at 10 mph. How much farther, in miles, does Grayson go in his motorboat compared to Rudy?"""
    grayson_distance = (1 * 25) + (0.5 * 20)  # distance in miles
    rudy_distance = 3 * 10  # distance in miles
    distance_difference = grayson_distance - rudy_distance
    result = distance_difference
    return result

print(solution())