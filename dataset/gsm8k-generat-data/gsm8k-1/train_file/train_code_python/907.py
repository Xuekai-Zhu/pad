def solution():
    """John runs a telethon to raise money. For the first 12 hours, he generates $5000 per hour. The remaining 14 hours, he generates 20% more per hour. How much total money does he make?"""
    first_12_hours = 12 * 5000
    percent_increase = 20
    increase_amount = first_12_hours * (percent_increase / 100)
    remaining_14_hours = (12 + 14) - 12
    new_hourly_rate = 5000 + (5000 * percent_increase / 100)
    money_in_remaining_hours = remaining_14_hours * new_hourly_rate
    total_money = first_12_hours + increase_amount + money_in_remaining_hours
    result = total_money
    return result

print(solution())