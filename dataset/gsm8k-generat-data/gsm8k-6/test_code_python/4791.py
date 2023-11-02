def solution():
    # Calculate the total sleep time of the cougar and zebra in one night
    cougar_sleep_time = 4
    zebra_sleep_time = cougar_sleep_time + 2

    # Calculate the total sleep time of the cougar and zebra in one week
    total_sleep_time = (cougar_sleep_time + zebra_sleep_time) * 7

    result = total_sleep_time
    return result

print(solution())