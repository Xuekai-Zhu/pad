def solution():
    # Calculate the total money raised in the first 12 hours
    first_half_money = 12 * 5000

    # Calculate the increased rate during the remaining 14 hours
    increased_rate = 1.20

    # Calculate the money raised per hour during the remaining 14 hours
    remaining_hours_money = 14 * 5000 * increased_rate

    # Calculate the total money raised during the telethon
    total_money = first_half_money + remaining_hours_money
    result = total_money
    return result

print(solution())