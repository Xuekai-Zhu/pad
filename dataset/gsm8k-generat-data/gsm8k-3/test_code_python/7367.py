def solution():
    """Eddy’s spider plant produces 2 baby plants 2 times a year.  After 4 years, how many baby plants will the mother plant have produced?"""
    # Define the number of baby plants produced per year
    BABY_PLANTS_PER_YEAR = 2 * 2

    # Define the number of years
    years = 4

    # Calculate the total number of baby plants produced
    total_baby_plants = BABY_PLANTS_PER_YEAR * years

    # Display the total number of baby plants
    result = total_baby_plants
    return result

print(solution())