def solution():
    night1 = 6  # Billy sleeps 6 hours on the first night
    night2 = night1 + 2  # Billy sleeps 2 more hours than the previous night on the second night
    night3 = night2 / 2  # Billy sleeps half of the previous night on the third night
    night4 = night3 * 3  # Billy sleeps triple the previous night on the fourth night

    # Calculate the total amount of sleep over four nights
    total_sleep = night1 + night2 + night3 + night4
    result = total_sleep
    return result

print(solution())