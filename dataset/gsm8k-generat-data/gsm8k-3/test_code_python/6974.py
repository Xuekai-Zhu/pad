def solution():
    """There are four members in one household. Each member consumes 3 slices of bread during breakfast and 2 slices of bread for snacks. A loaf of bread has 12 slices. How many days will five loaves of bread last in this family?"""
    # Define the number of slices each member consumes per day
    breakfast_slices = 3
    snack_slices = 2
    total_slices = breakfast_slices + snack_slices

    # Calculate the total number of slices consumed by the household per day
    slices_per_day = total_slices * 4

    # Calculate the total number of slices in five loaves of bread
    total_slices_bread = 5 * 12

    # Calculate the number of days the five loaves of bread will last
    days = total_slices_bread // slices_per_day

    # Display the number of days
    result = days
    return result

print(solution())