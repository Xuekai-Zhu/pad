def solution():
    
    # Define the number of slices in the loaf
    slices_in_loaf = 24

    # Define the number of slices Abby and Josh can eat per day
    slices_per_day_abby = 2
    slices_per_day_josh = slices_per_day_abby * 2

    # Calculate the number of days the loaf will last
    days_last = slices_in_loaf / (slices_per_day_abby + slices_per_day_josh)

    # Display the number of days the loaf will last
    result = days_last
    return result

print(solution())