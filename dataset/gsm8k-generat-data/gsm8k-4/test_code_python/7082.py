def solution():
    """Donna cut her pizza into 12 slices and ate half for lunch. She ate 1/3 of the remaining pizza for dinner. How many slices are left for Donna's lunch tomorrow?"""
    # Define the initial number of pizza slices
    pizza_slices = 12

    # Calculate the number of slices eaten for lunch
    lunch_slices = pizza_slices / 2

    # Calculate the number of slices remaining after lunch
    remaining_slices = pizza_slices - lunch_slices

    # Calculate the number of slices eaten for dinner
    dinner_slices = remaining_slices / 3

    # Calculate the number of slices remaining for lunch tomorrow
    lunch_slices_tomorrow = remaining_slices - dinner_slices

    # return the result
    result = lunch_slices_tomorrow
    return result

print(solution())