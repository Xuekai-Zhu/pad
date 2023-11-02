def solution():
    """There is a massive rainstorm lasting 4 days. There is an area that collects water to prevent flooding in the area. It ends up overflowing on the 4th day. The area can hold the equivalent of 6 feet of rain. It can also drain out the equivalent of 3 inches of rain per day to the nearby river without causing problems. The first day it rained 10 inches. The second day it rained twice that much. On the third day, it rained 50% more than the second day. It flooded the fourth day before getting a chance to do any of the draining. What is the minimum amount it rained on the fourth day?"""
    area_capacity = 6 * 12 # convert feet to inches
    drainage_per_day = 3
    total_rain_so_far = 10 + 2*10 + 1.5*2*10 # multiply by the percentage increase
    remaining_capacity = max(0, area_capacity - total_rain_so_far)
    minimum_rain_on_fourth_day = remaining_capacity + drainage_per_day*3 # multiply by the 3 remaining days
    result = minimum_rain_on_fourth_day
    return result

print(solution())