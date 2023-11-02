def solution():
    """Georgie needs 3 avocados to make her grandmother's guacamole recipe. If she already had 5 avocados and her sister buys another 4 avocados, how many servings of guacamole can Georgie make?"""
    # Define the number of avocados needed per serving
    avocados_per_serving = 3

    # Calculate the total number of avocados Georgie has
    total_avocados = 5 + 4

    # Calculate the number of servings of guacamole Georgie can make
    servings = total_avocados // avocados_per_serving

    # Display the result
    result = servings
    return result

print(solution())