def solution():
    """A charcoal grill burns fifteen coals to ash every twenty minutes of grilling. The grill ran for long enough to burn three bags of coals. Each bag of coal contains 60 coals. How long did the grill run?"""
    # Define the number of coals burned in 20 minutes
    COALS_PER_20_MINUTES = 15

    # Define the number of coals in each bag
    COALS_PER_BAG = 60

    # Calculate the total number of coals burned
    total_coals_burned = COALS_PER_BAG * 3

    # Calculate the total number of 20 minute intervals
    intervals = total_coals_burned / COALS_PER_20_MINUTES

    # Convert the number of intervals to hours and minutes
    hours = int(intervals / 3)
    minutes = int(intervals % 3 * 20)

    # Display the total time the grill ran
    result = f"{hours} hours and {minutes} minutes"
    return result

print(solution())