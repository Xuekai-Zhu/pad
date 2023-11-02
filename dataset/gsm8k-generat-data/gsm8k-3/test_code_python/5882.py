def solution():
    """On Saturdays and Sundays, Suzanne makes french toast for the family.  She and her husband each have 1 whole slice and her daughters split 1 slice.  She uses a thick sliced bread that comes 12 slices per loaf.  Over 52 weeks, how many loaves of bread will she need to make french toast?"""
    # Define the number of people eating french toast
    num_people = 4

    # Define the number of slices of bread per serving
    slices_per_serving = 2.5

    # Define the number of servings per weekend
    servings_per_weekend = 2

    # Calculate the number of slices of bread used per weekend
    slices_per_weekend = num_people * slices_per_serving * servings_per_weekend

    # Calculate the number of loaves of bread used per weekend
    loaves_per_weekend = slices_per_weekend / 12

    # Calculate the number of loaves of bread used over 52 weeks
    loaves_per_year = loaves_per_weekend * 52

    # Display the number of loaves of bread needed
    result = loaves_per_year
    return result

print(solution())