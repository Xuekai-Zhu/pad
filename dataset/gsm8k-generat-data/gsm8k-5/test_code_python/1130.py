def solution():
    # Calculate the total packages delivered during the week
    max_daily_deliveries = 35
    max_deliveries_twice = 2 * max_daily_deliveries
    unloading_packages = 50
    one_seventh_daily_perf = max_daily_deliveries / 7
    four_fifth_daily_perf = int(max_daily_deliveries * 4 / 5)
    total_deliveries = max_deliveries_twice + unloading_packages + one_seventh_daily_perf + four_fifth_daily_perf

    # Calculate the maximum possible packages Max could deliver during the week
    max_possible_deliveries = 7 * max_daily_deliveries

    # Calculate the difference between the maximum possible deliveries and the actual deliveries
    difference = max_possible_deliveries - total_deliveries
    result = difference
    return result

print(solution())