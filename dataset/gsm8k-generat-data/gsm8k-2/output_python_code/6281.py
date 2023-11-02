def solution():
    """
    There is a massive rainstorm lasting 4 days. There is an area that collects water to prevent flooding in the area.
    It ends up overflowing on the 4th day. The area can hold the equivalent of 6 feet of rain. It can also drain out
    the equivalent of 3 inches of rain per day to the nearby river without causing problems. The first day it rained
    10 inches. The second day it rained twice that much. On the third day, it rained 50% more than the second day.
    It flooded the fourth day before getting a chance to do any of the draining. What is the minimum amount it rained
    on the fourth day?
    """
    max_rain = 6 * 12  # 6 feet in inches
    drained_rain = 3 * 4  # 3 inches per day for 4 days
    total_drainable_rain = max_rain + drained_rain  # amount that can be held and drained
    first_day_rain = 10
    second_day_rain = 2 * first_day_rain
    third_day_rain = 1.5 * second_day_rain
    total_rain = first_day_rain + second_day_rain + third_day_rain  # total rain in first three days
    fourth_day_rain = max(0, total_rain + drained_rain - total_drainable_rain)  # minimum amount of rain on fourth day

    result = fourth_day_rain
    return result

print(solution())