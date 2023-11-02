def solution():
    """Grayson drives a motorboat for 1 hour at 25 mph and then 0.5 hours for 20 mph. Rudy rows in his rowboat for 3 hours at 10 mph. How much farther, in miles, does Grayson go in his motorboat compared to Rudy?"""
    # Calculate the distance traveled by Grayson in the motorboat
    grayson_distance = 25 * 1 + 20 * 0.5

    # Calculate the distance traveled by Rudy in the rowboat
    rudy_distance = 10 * 3

    # Calculate the difference in distance traveled
    distance_difference = grayson_distance - rudy_distance

    # Display the difference in distance traveled
    result = distance_difference
    return result

print(solution())