def solution():
    """There is a massive rainstorm lasting 4 days.  There is an area that collects water to prevent flooding in the area.  It ends up overflowing on the 4th day.  The area can hold the equivalent of 6 feet of rain.  It can also drain out the equivalent of 3 inches of rain per day to the nearby river without causing problems.  The first day it rained 10 inches.  The second day it rained twice that much.  On the third day, it rained 50% more than the second day.  It flooded the fourth day before getting a chance to do any of the draining.  What is the minimum amount it rained on the fourth day?"""
    # Define the capacity of the water collecting area in inches and the daily drainage rate in inches
    CAPACITY = 6 * 12  # in inches
    DRAINAGE_RATE = 3  # in inches per day

    # Calculate the total rainfall for the first three days
    rainfall1 = 10  # inches
    rainfall2 = 2 * rainfall1
    rainfall3 = rainfall2 * 1.5
    total_rainfall = rainfall1 + rainfall2 + rainfall3

    # Calculate the remaining capacity of the water collecting area after the first three days
    remaining_capacity = CAPACITY - total_rainfall

    # Calculate the maximum amount of rainfall that can be accommodated before overflowing
    max_rainfall = remaining_capacity + DRAINAGE_RATE * 3  # 3 days of drainage assumed

    # Calculate the minimum amount of rainfall on the fourth day that can cause overflowing
    min_rainfall = max_rainfall - total_rainfall

    # Display the minimum amount of rainfall on the fourth day
    result = min_rainfall
    return result

print(solution())