def solution():
    """To make fried green tomatoes, Thelma cuts each green tomato into 8 slices before cooking them up.  If 20 slices of fried green tomato make a meal for a single person, how many tomatoes will Thelma need to make enough fried green tomatoes to feed a family of 8 for a single meal?"""
    # Define the number of slices needed for a single meal
    slices_per_meal = 20

    # Calculate the total number of slices needed for a family of 8
    total_slices = slices_per_meal * 8

    # Calculate the number of tomatoes needed
    tomatoes_needed = total_slices / 8

    # Round up to the nearest whole tomato
    tomatoes_needed = int(tomatoes_needed) + 1

    # return the result
    result = tomatoes_needed
    return result

print(solution())