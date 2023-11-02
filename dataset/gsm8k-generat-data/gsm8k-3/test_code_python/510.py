def solution():
    """A pie shop charges $3 per slice of custard pie. They cut each whole pie into 10 slices. If they make 6 whole custard pies, how much money will the pie shop earn?"""
    # Define the price per slice of pie and the number of pies made
    PRICE_PER_SLICE = 3
    NUM_PIES = 6

    # Calculate the number of slices in all the pies
    num_slices = NUM_PIES * 10

    # Calculate the total earnings
    earnings = num_slices * PRICE_PER_SLICE

    # Display the total earnings
    result = earnings
    return result

print(solution())