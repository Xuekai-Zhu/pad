def solution():
    """Each year Dani gets 4 pairs of two pants each as pay winning the best Amazon buyer of the season.
    If he initially had 50 pants, calculate the number of pants he'll have in 5 years."""
    # Define the initial number of pants
    initial_pants = 50

    # Define the number of pairs of pants Dani gets each year
    pants_per_year = 4 * 2

    # Calculate the total number of pants Dani will have in 5 years
    total_pants = initial_pants + (5 * pants_per_year)

    result = total_pants
    return result

print(solution())