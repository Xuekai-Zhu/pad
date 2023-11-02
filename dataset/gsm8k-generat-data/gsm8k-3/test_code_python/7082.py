def solution():
    """Donna cut her pizza into 12 slices and ate half for lunch.  She ate 1/3 of the remaining pizza for dinner.  How many slices are left for Donna's lunch tomorrow?"""
    # Define the number of slices in the pizza
    total_slices = 12

    # Calculate the number of slices Donna ate for lunch
    lunch_slices = total_slices / 2

    # Calculate the number of slices remaining after lunch
    remaining_slices = total_slices - lunch_slices

    # Calculate the number of slices Donna ate for dinner
    dinner_slices = remaining_slices / 3

    # Calculate the number of slices remaining for tomorrow's lunch
    tomorrow_slices = remaining_slices - dinner_slices

    # Display the number of slices remaining for tomorrow's lunch
    result = tomorrow_slices
    return result

print(solution())