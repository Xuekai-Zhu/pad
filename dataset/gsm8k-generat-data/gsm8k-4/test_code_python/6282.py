def solution():
    """There is a massive rainstorm lasting 4 days. There is an area that collects water to prevent flooding in the area. It ends up overflowing on the 4th day. The area can hold the equivalent of 6 feet of rain. It can also drain out the equivalent of 3 inches of rain per day to the nearby river without causing problems. The first day it rained 10 inches. The second day it rained twice that much. On the third day, it rained 50% more than the second day. It flooded the fourth day before getting a chance to do any of the draining. What is the minimum amount it rained on the fourth day?"""
    # Define the maximum amount of rain the area can hold, in inches
    max_rain = 6 * 12

    # Define the amount of rain that has already fallen on the first three days
    rain_so_far = 10 + 2*10 + 1.5*2*10

    # Calculate the remaining capacity of the area for the fourth day
    remaining_capacity = max_rain - rain_so_far

    # Subtract the amount of rain that can be drained out without causing problems
    remaining_capacity -= 3*4

    # Calculate the minimum amount it needs to rain on the fourth day to trigger the overflow
    overflow_amount = max(0, remaining_capacity)

    result = overflow_amount / 4
    return result

print(solution())