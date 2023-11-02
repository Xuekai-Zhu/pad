def solution():
    # Calculate the total money John makes during the first 12 hours
    money_first_12_hours = 12 * 5000

    # Calculate the increased rate of generating money for the remaining 14 hours
    increased_rate = 1.2 * 5000

    # Calculate the total money John makes during the remaining 14 hours
    money_remaining_14_hours = 14 * increased_rate

    # Calculate the total money John makes during the entire telethon
    total_money = money_first_12_hours + money_remaining_14_hours
    result = total_money
    return result

print(solution())