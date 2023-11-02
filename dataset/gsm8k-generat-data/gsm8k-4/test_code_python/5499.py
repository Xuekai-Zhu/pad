def solution():
    """Grayson drives a motorboat for 1 hour at 25 mph and then 0.5 hours for 20 mph. Rudy rows in his rowboat for 3 hours at 10 mph. How much farther, in miles, does Grayson go in his motorboat compared to Rudy?"""
    # Calculate the distance Grayson travels in the first hour
    grayson_dist_1 = 25 * 1

    # Calculate the distance Grayson travels in the second half hour
    grayson_dist_2 = 20 * 0.5

    # Add the distances to get the total distance Grayson travels
    grayson_dist_total = grayson_dist_1 + grayson_dist_2

    # Calculate the distance Rudy travels in 3 hours
    rudy_dist_total = 10 * 3

    # Calculate the difference in distance between Grayson and Rudy
    distance_diff = grayson_dist_total - rudy_dist_total

    result = distance_diff
    return result

print(solution())