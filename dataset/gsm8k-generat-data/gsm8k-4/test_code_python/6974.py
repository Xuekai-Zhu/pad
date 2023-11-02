def solution():
    """There are four members in one household. Each member consumes 3 slices of bread during breakfast and 2 slices of bread for snacks. A loaf of bread has 12 slices. How many days will five loaves of bread last in this family?"""
    # Define the number of family members and the number of slices of bread they consume per day
    family_members = 4
    breakfast_slices = 3
    snack_slices = 2

    # Calculate the total number of slices of bread consumed by the family per day
    total_slices_per_day = family_members * (breakfast_slices + snack_slices)

    # Define the number of slices per loaf of bread
    slices_per_loaf = 12

    # Calculate the total number of slices consumed by the family in 5 days
    total_slices_5_days = total_slices_per_day * 5

    # Calculate the number of loaves of bread needed for 5 days
    loaves_5_days = total_slices_5_days / slices_per_loaf

    # Return the result
    result = loaves_5_days
    return result

print(solution())