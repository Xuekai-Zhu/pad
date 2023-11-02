def solution():
    # Calculate the money generated in the first 12 hours
    money_first_12_hours = 12 * 5000

    # Calculate the percentage increase for the remaining 14 hours
    percentage_increase = 20 / 100

    # Calculate the hourly rate for the remaining 14 hours
    hourly_rate = 5000 + (5000 * percentage_increase)

    # Calculate the money generated for the remaining 14 hours
    money_remaining_14_hours = 14 * hourly_rate

    # Calculate the total money generated
    total_money = money_first_12_hours + money_remaining_14_hours
    result = total_money
    return result

print(solution())