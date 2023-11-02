def solution():
    """Grayson drives a motorboat for 1 hour at 25 mph and then 0.5 hours for 20 mph. Rudy rows in his rowboat for 3 hours at 10 mph. How much farther, in miles, does Grayson go in his motorboat compared to Rudy?"""
    grayson_distance = 25 * 1 + 20 * 0.5
    rudy_distance = 10 * 3
    difference = grayson_distance - rudy_distance
    result = difference
    return result

print(solution())