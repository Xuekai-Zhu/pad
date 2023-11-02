def solution():
    """To make fried green tomatoes, Thelma cuts each green tomato into 8 slices before cooking them up.  If 20 slices of fried green tomato make a meal for a single person, how many tomatoes will Thelma need to make enough fried green tomatoes to feed a family of 8 for a single meal?"""
    # Define the number of slices per tomato and number of people in the family
    SLICES_PER_TOMATO = 8
    FAMILY_SIZE = 8

    # Calculate the total number of slices needed for the family
    slices_needed = 20 * FAMILY_SIZE

    # Calculate the number of tomatoes needed
    tomatoes_needed = slices_needed / SLICES_PER_TOMATO

    # Round up to the nearest whole tomato
    tomatoes_needed = int(tomatoes_needed) + (tomatoes_needed % 1 > 0)

    # Display the number of tomatoes needed
    result = tomatoes_needed
    return result

print(solution())