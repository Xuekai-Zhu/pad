def solution():
    """Eddy's spider plant produces 2 baby plants 2 times a year. After 4 years, how many baby plants will the mother plant have produced?"""
    # Define the initial number of baby plants and the number of baby plant production cycles per year
    baby_plants = 0
    cycles_per_year = 2

    # Iterate over the number of years and calculate the total number of baby plants produced
    for year in range(1, 5):
        # Calculate the number of baby plants produced in each cycle
        baby_plants_per_cycle = baby_plants + cycles_per_year * 2

        # Update the total number of baby plants
        baby_plants += baby_plants_per_cycle

    # Return the total number of baby plants produced
    result = baby_plants
    return result

print(solution())