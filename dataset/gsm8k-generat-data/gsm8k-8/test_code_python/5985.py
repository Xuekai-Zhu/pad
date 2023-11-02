def solution():
    # Calculate the amount of sleep each night
    night1_sleep = 6
    night2_sleep = night1_sleep + 2
    night3_sleep = night2_sleep / 2
    night4_sleep = night3_sleep * 3

    # Calculate the total amount of sleep over four nights
    total_sleep = night1_sleep + night2_sleep + night3_sleep + night4_sleep
    result = total_sleep
    return result

print(solution())