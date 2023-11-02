def solution():
    # Calculate the total money generated in the first 12 hours
    first_12_hours = 12 * 5000

    # Calculate the increased rate for the remaining 14 hours
    increased_rate = 1.2

    # Calculate the total money generated in the remaining 14 hours
    remaining_14_hours = 14 * 5000 * increased_rate

    # Calculate the total money generated for the entire telethon
    total_money_generated = first_12_hours + remaining_14_hours
    result = total_money_generated
    return result

print(solution())