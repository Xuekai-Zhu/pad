def solution():
    """On Saturdays and Sundays, Suzanne makes french toast for the family. She and her husband each have 1 whole slice and her daughters split 1 slice. She uses a thick sliced bread that comes 12 slices per loaf. Over 52 weeks, how many loaves of bread will she need to make french toast?"""
    # Define the number of french toast made each weekend
    french_toast_per_weekend = 1 + 1 + 0.5 + 0.5

    # Define the number of weekends in a year
    weekends_per_year = 52

    # Define the number of slices of bread needed to make one weekend's french toast
    slices_per_weekend = french_toast_per_weekend * 2

    # Define the number of slices of bread per loaf
    slices_per_loaf = 12

    # Calculate the number of loaves needed for one weekend's french toast
    loaves_per_weekend = slices_per_weekend / slices_per_loaf

    # Calculate the total number of loaves needed for a year's worth of french toast
    loaves_per_year = loaves_per_weekend * weekends_per_year

    # return the result
    result = int(loaves_per_year)
    return result

print(solution())