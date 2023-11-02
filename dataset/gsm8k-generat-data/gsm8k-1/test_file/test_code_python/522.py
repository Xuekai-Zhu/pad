def solution():
    """Ada's daily electric consumption is 12 kilowatts per hour. She is planning to add a device that will consume 2 kilowatts per hour a day. If a kilowatt per hour is $1.50, how much is the difference between Ada's weekly electric bill before and after she adds the new device?"""
    daily_usage_before = 12
    daily_usage_after = 12 + 2
    price_per_kwh = 1.5
    daily_cost_before = daily_usage_before * price_per_kwh
    daily_cost_after = daily_usage_after * price_per_kwh
    weekly_difference = (daily_cost_after - daily_cost_before) * 7
    result = weekly_difference
    return result

print(solution())