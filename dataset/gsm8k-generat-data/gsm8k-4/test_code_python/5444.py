def solution():
    """It rained twice as much on Tuesday as Monday. On Monday it rained 3 inches more than Sunday. It rained 4 inches on Sunday. How much total rainfall was there over the 3 days?"""
    # Define the rainfall on Sunday
    sunday_rainfall = 4

    # Calculate the rainfall on Monday
    monday_rainfall = sunday_rainfall + 3

    # Calculate the rainfall on Tuesday
    tuesday_rainfall = 2 * monday_rainfall

    # Calculate the total rainfall over the 3 days
    total_rainfall = sunday_rainfall + monday_rainfall + tuesday_rainfall

    # Return the result
    result = total_rainfall
    return result

print(solution())